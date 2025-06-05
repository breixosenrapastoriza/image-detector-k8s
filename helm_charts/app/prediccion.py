from PIL import Image
from io import BytesIO
import numpy as np
import boto3
import os
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, decode_predictions

input_shape = (224, 224, 3)
bucket_name = 'cdap-db'

def load_model():
    model = MobileNetV2(weights='imagenet', input_shape=input_shape)
    return model

_model = load_model()

def read_image(image_encoded):
    image = Image.open(BytesIO(image_encoded)).convert("RGB")
    return image

def preprocess_image(image: Image.Image):
    image = image.resize((224, 224))
    image_array = np.array(image, dtype=np.float32)
    image_array = (image_array / 127.5) - 1.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

def predict(image: np.ndarray):
    prediction = _model.predict(image)
    decoded_predictions = decode_predictions(prediction, top=1)[0]
    label, description, probability = decoded_predictions[0]
    return label, description.replace(" ", "_").lower(), probability

def upload_to_s3(image_encoded, folder_name, filename):
    s3 = boto3.client('s3')
    key = f"{folder_name}/{filename}"
    s3.upload_fileobj(BytesIO(image_encoded), bucket_name, key)
