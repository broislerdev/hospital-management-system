# 🏥 Hospital Management System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A CLI-based hospital management system built with Python and OOP principles. Manage patients, doctors, and appointments directly from the terminal — with persistent data storage using JSON.



## 🚀 How to run

Make sure you have Python installed, then run in your terminal:





```
py main.py
```



## 🕹️ Features

- 👤 **Patients** — register, search, list and remove patients
- 🩺 **Doctors** — register, search, list and remove doctors with CRM duplicate validation
- 📅 **Appointments** — schedule, list by patient or doctor, and cancel appointments
- 💾 **Persistence** — data is automatically saved to a JSON file on exit and loaded on startup
- 🛡️ **Input validation** — handles invalid inputs with try/except blocks



## 🗂️ Project Structure

```
hospital-management-system/
├── main.py          # CLI menu and user interaction
├── hospital.py      # Hospital class — business logic
├── models.py        # Patient, Doctor and Appointment classes
├── .gitignore
└── README.md
```



## 🧠 Concepts applied

- Object-Oriented Programming (OOP)
- Separation of concerns
- JSON serialization and deserialization
- Error handling with try/except
- Data persistence



## 🛠️ Built with

- Python (no external libraries)
