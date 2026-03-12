
# Face Recognition Attendance System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

A **real-time Face Recognition Attendance System** built using **Machine Learning, Deep Learning, and Computer Vision**.  
The system automatically detects faces through a webcam, identifies the person, and records attendance without manual input.

This project was developed as part of the **M.Sc. Data Science program at Osmania University**. :contentReference[oaicite:0]{index=0}

---

# Project Demo

Add screenshots or GIFs of the system here.

```

/screenshots
├── detection.png
├── recognition.png
└── attendance_sheet.png

```

Example:

| Face Detection | Face Recognition | Attendance Output |
|---|---|---|
| Add Screenshot | Add Screenshot | Add Screenshot |

---

# Project Overview

Traditional attendance systems such as manual registers or biometric devices have limitations such as:

- Time consuming
- Proxy attendance
- Hardware dependency
- Maintenance costs

This project implements an **AI-based automated attendance system using facial recognition**. The system detects faces, extracts facial features, compares them with stored embeddings, and records attendance automatically.

The model uses **CNN-based face embedding techniques such as FaceNet** for high recognition accuracy. :contentReference[oaicite:1]{index=1}

---

# Key Features

- Real-time face detection using webcam
- Automatic identity recognition
- Attendance saved in CSV/Excel format
- High accuracy using deep learning
- Confidence score display
- Easy user registration for new faces
- Real-time processing

---

# System Architecture

```

Input Image / Webcam
│
▼
Face Detection
(Haar Cascade / MTCNN)
│
▼
Face Alignment & Cropping
│
▼
Image Preprocessing
(Resize, Normalize)
│
▼
Feature Extraction
(CNN / FaceNet)
│
▼
Face Recognition
(Similarity Matching)
│
▼
Attendance Logging
(CSV / Excel)

```

This pipeline enables **real-time face recognition and attendance recording**. :contentReference[oaicite:2]{index=2}

---

# Technologies Used

## Programming Language
- Python

## Machine Learning / Deep Learning
- CNN (Convolutional Neural Networks)
- FaceNet
- VGGFace
- SVM
- KNN

## Computer Vision
- OpenCV
- dlib
- MTCNN

## Libraries
- NumPy
- Pandas
- TensorFlow / Keras
- Matplotlib
- Scikit-learn

## Deployment
- Streamlit / Flask

---

# Dataset

The system is trained using benchmark face datasets:

- **LFW (Labeled Faces in the Wild)**  
  - 13,233 images
  - 5,749 individuals

- **CASIA-WebFace**

- **VGGFace2**

These datasets include variations in **pose, lighting, expression, and occlusion**, which improve model robustness. :contentReference[oaicite:3]{index=3}

---

# Project Structure

```

Face-Recognition-Attendance-System
│
├── dataset
│   └── training_images
│
├── models
│   └── face_model.pkl
│
├── attendance
│   └── attendance.csv
│
├── src
│   ├── face_detection.py
│   ├── face_recognition.py
│   ├── preprocessing.py
│   └── attendance_system.py
│
├── screenshots
│
├── app.py
├── requirements.txt
└── README.md

````

---

# Installation

## 1 Clone the Repository

```bash
git clone https://github.com/yourusername/face-recognition-attendance-system.git
cd face-recognition-attendance-system
````

---

## 2 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3 Run the Application

```bash
python app.py
```

or

```bash
streamlit run app.py
```

---

# Requirements

Minimum hardware requirements:

| Component | Minimum            |
| --------- | ------------------ |
| CPU       | Intel i5 / Ryzen 5 |
| RAM       | 8 GB               |
| Storage   | 256 GB             |
| Webcam    | Required           |

Recommended:

* GPU (NVIDIA CUDA supported) for faster training.

---

# Performance Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC Curve
* Confusion Matrix

These metrics help evaluate recognition reliability and system performance. 

---

# Applications

* Smart classroom attendance
* Office employee attendance system
* Secure access control
* Identity verification systems
* Surveillance systems

---

# Limitations

* Performance affected by low lighting
* Requires sufficient training data
* Privacy concerns with biometric systems
* High computational requirements for deep learning models

---

# Future Improvements

* Mobile app integration
* Cloud database for attendance
* Anti-spoofing detection
* Mask detection
* Multi-camera support
* Edge device deployment (Raspberry Pi)

---

# Contributors

* Akash Kumar Pandey

Supervisor
Ms. M. Anusha
Aurora’s Degree & PG College
Osmania University

---

# License

This project is developed for **academic and research purposes only**.

