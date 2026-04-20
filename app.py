import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("🏥 Medical Record Management System")

menu = ["Add Patient", "View Patients", "Search Patient"]
choice = st.sidebar.selectbox("Menu", menu)

# =========================
# ➕ Add Patient
# =========================
if choice == "Add Patient":
    st.subheader("Add New Patient")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    disease = st.text_input("Disease")
    doctor = st.text_input("Doctor")

    if st.button("Add Patient"):
        data = {
            "name": name,
            "age": age,
            "disease": disease,
            "doctor": doctor
        }

        response = requests.post(f"{BASE_URL}/add_patient", json=data)

        if response.status_code == 200:
            st.success("✅ Patient Added Successfully")
        else:
            st.error("❌ Error adding patient")

# =========================
# 📋 View Patients
# =========================
elif choice == "View Patients":
    st.subheader("All Patients")

    if st.button("Fetch Patients"):
        response = requests.get(f"{BASE_URL}/patients")

        if response.status_code == 200:
            patients = response.json()
            for p in patients:
                st.write(p)
        else:
            st.error("❌ Failed to fetch data")

# =========================
# 🔍 Search Patient
# =========================
elif choice == "Search Patient":
    st.subheader("Search Patient by Name")

    search_name = st.text_input("Enter Name")

    if st.button("Search"):
        response = requests.get(f"{BASE_URL}/patient/{search_name}")

        if response.status_code == 200:
            results = response.json()

            if results:
                for r in results:
                    st.write(r)
            else:
                st.warning("No patient found")
        else:
            st.error("❌ Error searching patient")