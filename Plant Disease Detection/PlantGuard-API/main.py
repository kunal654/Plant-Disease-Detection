from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Plant Disease Analysis API")

# Load model and labels at startup
MODEL_PATH = "keras_model1.h5"
LABELS_PATH = "labels.txt"

model = load_model(MODEL_PATH, compile=False)
class_names = open(LABELS_PATH, "r").readlines()

# Disease Cures and Removal Processes
disease_info = {
    "Healthy Tomato": {
        "cure": "No treatment needed. Maintain proper care and watering.",
        "removal_process": "Keep monitoring the plant and ensure regular watering."
    },
    "Tomato Mosaic Virus": {
        "cure": "Remove infected plants immediately. Disinfect tools. Use resistant varieties.",
        "removal_process": "Burn or bury infected plants to prevent spread. Disinfect tools with bleach after use."
    },
    "Tomato Yellow Leaf Curl Virus": {
        "cure": "Control whiteflies with insecticides. Remove infected plants.",
        "removal_process": "Use insecticidal soap or neem oil to kill whiteflies. Introduce beneficial insects like ladybugs."
    },
    "Target Spot": {
        "cure": "Apply fungicides like chlorothalonil. Rotate crops and remove infected leaves.",
        "removal_process": "Ensure proper spacing between plants for good air circulation. Use drip irrigation instead of overhead watering."
    },
    "Spider Mites (Two-Spotted)": {
        "cure": "Use neem oil or insecticidal soap. Introduce predatory mites.",
        "removal_process": "Spray leaves with water to knock off mites. Keep humidity high to discourage mites."
    },
    "Septoria Leaf Spot": {
        "cure": "Apply copper-based fungicides. Remove infected leaves and avoid overhead watering.",
        "removal_process": "Prune lower leaves and remove debris to prevent fungal spread. Rotate crops annually."
    },
    "Leaf Mold": {
        "cure": "Improve air circulation, use resistant varieties, and apply fungicides if necessary.",
        "removal_process": "Ensure proper ventilation in greenhouses. Remove and destroy infected leaves."
    },
    "Late Blight": {
        "cure": "Apply fungicides like chlorothalonil or mancozeb. Remove infected plants.",
        "removal_process": "Uproot and destroy infected plants. Avoid planting tomatoes in the same spot next season."
    },
    "Early Blight": {
        "cure": "Use fungicides and practice crop rotation. Remove infected leaves.",
        "removal_process": "Mulch around the base of plants to prevent soil splash. Space plants properly to improve airflow."
    },
    "Bacterial Spot": {
        "cure": "Use copper-based bactericides. Avoid overhead irrigation and remove infected leaves.",
        "removal_process": "Disinfect gardening tools. Do not use seeds from infected plants."
    }
}

@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/docs", status_code=308)

@app.post("/predict/")
def predict_image(file: UploadFile = File(...)):
    try:
        # Open and preprocess the image
        image = Image.open(file.file).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array

        # Perform prediction
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index].strip()  # Remove newline characters
        confidence_score = float(prediction[0][index])

        # Get cure and removal process
        disease_data = disease_info.get(class_name, {
            "cure": "Information not available.",
            "removal_process": "Consult an agricultural expert."
        })

        # Return the prediction as JSON
        return JSONResponse(
            content={
                "class_name": class_name,
                "confidence_score": confidence_score,
                "cure": disease_data["cure"],
                "removal_process": disease_data["removal_process"]
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))