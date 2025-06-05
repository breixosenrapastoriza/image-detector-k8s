# FastAPI app definition

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from prediccion import read_image, preprocess_image, predict, upload_to_s3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/predict")
async def predict_image(file: UploadFile = File(...)):
    try:
        image_encoded = await file.read()
        image = read_image(image_encoded)
        preprocessed_image = preprocess_image(image)

        label, description, probability = predict(preprocessed_image)
        print("Prediction made successfully.")

        # Guardar en S3
        upload_to_s3(image_encoded, description, file.filename)

        return {
            "Predicted class": label,
            "Description": description,
            "Probability": f"{probability * 100:.2f}%"
        }

    except Exception as e:
        return {"error": str(e)}
