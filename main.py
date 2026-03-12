import cv2
from deepface import DeepFace
import os
from datetime import datetime
import numpy as np

# Folder with known face images (e.g., known_faces/Praveen.jpg)
KNOWN_DIR = "known_faces"
ATTENDANCE_FILE = "attendance.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(ATTENDANCE_FILE):
    with open(ATTENDANCE_FILE, "w") as f:
        f.write("Name,Time\n")

# Load known faces into memory
known_embeddings = {}
for file in os.listdir(KNOWN_DIR):
    if file.lower().endswith((".jpg", ".png")):
        path = os.path.join(KNOWN_DIR, file)
        name = os.path.splitext(file)[0]
        try:
            embedding = DeepFace.represent(img_path=path, model_name="Facenet", enforce_detection=True)[0]["embedding"]
            known_embeddings[name] = embedding
        except Exception as e:
            print(f"Error processing {file}: {e}")

# Compare function
def recognize_face(frame):
    try:
        target_embedding = DeepFace.represent(frame, model_name="Facenet", enforce_detection=False)[0]["embedding"]
        for name, emb in known_embeddings.items():
            distance = np.linalg.norm(np.array(emb) - np.array(target_embedding))
            if distance < 10:  # Lower = more similar; adjust threshold if needed
                return name
    except Exception as e:
        print("Detection error:", e)
    return "Unknown"

# Mark attendance
def mark_attendance(name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ATTENDANCE_FILE, "a") as f:
        f.write(f"{name},{now}\n")

# Start webcam
cap = cv2.VideoCapture(0)
print("Starting webcam. Press ESC to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    name = recognize_face(frame)
    if name != "Unknown":
        mark_attendance(name)

    cv2.putText(frame, name, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()

