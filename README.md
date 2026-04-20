# 🏥 Medical Record Management System

## 📌 Overview

This project is a simple **Medical Record Management System** built using FastAPI and Streamlit.
It allows users to add, view, and search patient records stored in Firebase Firestore.

---

## 🚀 Features

* ➕ Add new patient records
* 📋 View all patients
* 🔍 Search patient by name
* ☁️ Data stored in Firebase Firestore

---

## 🛠️ Tech Stack

* FastAPI (Backend API)
* Streamlit (Frontend UI)
* Firebase Firestore (Database)
* Requests (API communication)

---

## 📂 Project Structure

```
project/
│
├── main.py          # FastAPI backend
├── app.py           # Streamlit frontend
├── requirements.txt
├── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd <your-repo-folder>
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Firebase Setup

1. Go to Firebase Console
2. Create a project
3. Enable Firestore Database
4. Generate a Service Account Key
5. Download the JSON file
6. Rename it to:

```
serviceAccountKey.json
```

7. Place it in the project root folder

---

### 4. Run FastAPI server

```
uvicorn main:app --reload
```

---

### 5. Run Streamlit app

```
streamlit run app.py
```

---

## 🌐 API Endpoints

| Method | Endpoint        | Description      |
| ------ | --------------- | ---------------- |
| POST   | /add_patient    | Add new patient  |
| GET    | /patients       | Get all patients |
| GET    | /patient/{name} | Search patient   |

---

## ⚠️ Note

* Do NOT upload `serviceAccountKey.json` to GitHub
* Add it to `.gitignore`

---

## 📌 Future Improvements

* Update/Delete patient records
* Authentication system
* Deployment using cloud platforms

---

## 👩‍💻 Author

Harini Muthukumar
# Medical-Record-Management-System-Using-NoSQL
