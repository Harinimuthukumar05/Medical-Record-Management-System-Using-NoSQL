from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

app = FastAPI()

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Add Patient
@app.post("/add_patient")
def add_patient(patient: dict):
    db.collection("patients").add(patient)
    return {"message": "Patient added successfully"}

# Get All Patients
@app.get("/patients")
def get_patients():
    docs = db.collection("patients").stream()
    return [doc.to_dict() for doc in docs]

# Search Patient by Name
@app.get("/patient/{name}")
def get_patient(name: str):
    docs = db.collection("patients").where("name", "==", name).stream()
    return [doc.to_dict() for doc in docs]