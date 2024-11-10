# attendance.py
import cv2
import face_recognition
import pickle
import pandas as pd
from datetime import datetime

# Load encodings
with open('encodings.pkl', 'rb') as file:
    data = pickle.load(file)

known_encodings = data['encodings']
known_names = data['names']

# Initialize attendance DataFrame
try:
    attendance_df = pd.read_csv('attendance.csv')
except FileNotFoundError:
    attendance_df = pd.DataFrame(columns=['Name', 'Time'])

def mark_attendance(name):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    attendance_df.loc[len(attendance_df)] = [name, current_time]
    attendance_df.to_csv('attendance.csv', index=False)
    print(f"Marked attendance for {name} at {current_time}")

# Start webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = face_distances.argmin()

        if matches[best_match_index]:
            name = known_names[best_match_index]

        # Draw a rectangle around the face
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Mark attendance if a known face is detected
        if name != "Unknown":
            if name not in attendance_df['Name'].values:
                mark_attendance(name)

    cv2.imshow('Face Recognition Attendance', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
video_capture.release()
cv2.destroyAllWindows()