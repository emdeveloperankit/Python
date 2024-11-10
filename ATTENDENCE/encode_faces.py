# encode_faces.py
import os
import face_recognition
import pickle

def encode_faces():
    known_encodings = []
    known_names = []
    
    # Loop through each folder in the 'images' directory
    for person in os.listdir('images'):
        person_folder = os.path.join('images', person)
        
        # Loop through each image of the person
        for image_file in os.listdir(person_folder):
            image_path = os.path.join(person_folder, image_file)
            print(f"Processing {image_path}")
            
            # Load and encode the image
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(person)
    
    # Save encodings and names
    with open('encodings.pkl', 'wb') as file:
        pickle.dump({'encodings': known_encodings, 'names': known_names}, file)

    print("Encoding completed!")

if __name__ == "__main__":
    encode_faces()
