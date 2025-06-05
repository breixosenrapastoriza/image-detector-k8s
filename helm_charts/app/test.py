import pytest
from unittest.mock import patch, MagicMock
from prediccion import read_image, preprocess_image, predict, upload_to_s3
from PIL import Image
import numpy as np
from io import BytesIO
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Imagen dummy para pruebas
def dummy_image_bytes():
    img = Image.new("RGB", (300, 300), color="red")
    buf = BytesIO()
    img.save(buf, format='JPEG')
    return buf.getvalue()

def test_read_image():
    image_bytes = dummy_image_bytes()
    image = read_image(image_bytes)
    assert isinstance(image, Image.Image)
    assert image.mode == "RGB"

def test_preprocess_image():
    img = Image.new("RGB", (300, 300), color="blue")
    processed = preprocess_image(img)
    assert processed.shape == (1, 224, 224, 3)
    assert processed.dtype == np.float32

def test_predict():
    img = Image.new("RGB", (224, 224), color="green")
    processed = preprocess_image(img)
    label, desc, prob = predict(processed)
    assert isinstance(label, str)
    assert isinstance(desc, str)
    assert isinstance(prob, float)

@patch("prediccion.boto3.client")
def test_upload_to_s3(mock_boto_client):
    mock_s3 = MagicMock()
    mock_boto_client.return_value = mock_s3
    image_bytes = dummy_image_bytes()
    upload_to_s3(image_bytes, "test_folder", "test.jpg")
    mock_s3.upload_fileobj.assert_called_once()

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

@patch("prediccion.upload_to_s3")
def test_predict_endpoint(mock_upload):
    image_bytes = dummy_image_bytes()
    files = {"file": ("test.jpg", image_bytes, "image/jpeg")}
    response = client.post("/api/predict", files=files)
    assert response.status_code == 200
    json_data = response.json()
    assert "Predicted class" in json_data
    assert "Description" in json_data
    assert "Probability" in json_data
