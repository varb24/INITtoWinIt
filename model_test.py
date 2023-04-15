import cv2
import numpy as np
import torch
import threading
from joas_model import MyModel
from flask import Flask, request

# Set up the Flask app
app = Flask(__name__)

# Set up the camera input
cap = cv2.VideoCapture(0)

# Initialize face data dictionary
face_data = {}

# Load the facial recognition model
model = MyModel()
weights = torch.load('model_weights.pth', map_location=torch.device('cpu'))
model.load_state_dict(weights)

# Define functions
def preprocess(frame):
    # Preprocess the frame by converting it to grayscale and normalizing its pixel values
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    normalized = gray / 255.0
    return np.expand_dims(np.expand_dims(normalized, axis=0), axis=0)

def is_face(embeddings, face_data):
    # Check if the embeddings correspond to a face
    if len(embeddings) > 0:
        # Iterate through the stored face data
        for student_id, stored_embeddings in face_data.items():
            # Calculate the distance between the embeddings and the stored embeddings
            distance = np.linalg.norm(embeddings - stored_embeddings)
            if distance < 0.5:
                # The embeddings correspond to a stored face
                return student_id
        # The embeddings don't correspond to a stored face, so create a new ID and store the face data
        new_id = len(face_data) + 1
        face_data[new_id] = embeddings
        store_face(embeddings, new_id)
        print("New student ID created: ", new_id)
    return None

def store_face(embeddings, student_id):
    # Store the face data in a dictionary
    face_data[student_id] = embeddings
    # Write the face data to a file
    with open('face_embeddings.txt', 'a') as f:
        f.write(','.join([str(e) for e in embeddings]) + ',' + str(student_id) + '\n')

# Define face recognition loop
def recognize_faces():
    face_data = {}
    while True:
        # Capture a frame
        ret, frame = cap.read()

        # Preprocess the frame
        processed_frame = preprocess(frame)

        # Get the face embeddings for the processed frame
        with torch.no_grad():
            embeddings = model(torch.from_numpy(processed_frame))
            embeddings = embeddings.detach().numpy()[0]

        # Check if a face was recognized
        student_id = is_face(embeddings, face_data)
        if student_id:
            print("Student ID: ", student_id)
        else:
            # Face data does not exist, prompt user for student ID and store face data
            student_id = input("Student ID not found. Please enter the student ID: ")
            store_face(embeddings, student_id)

        # Show the image frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the memory and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Define face recognition API endpoint
@app.route('/recognize_face', methods=['POST'])
def recognize_face_api():
    # Capture a frame from the request
    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Preprocess the frame
    processed_frame = preprocess(img)

    # Get the face embeddings for the processed frame
    with torch.no_grad():
        embeddings = model(torch.from_numpy(processed_frame))
        embeddings = embeddings.detach().numpy()[0]

    # Check if a face was recognized
    student_id = is_face(embeddings, face_data)
    if student_id:
        return {'student_id': student_id}
    else:
        # Face data does not exist, return an error
        return {'error': 'Student ID not found.'}

if __name__ == '__main__':
    # Start the facial recognition loop in a separate thread
    face_thread = threading.Thread(target=recognize_faces)
    face_thread.daemon = True
    face_thread.start()

    # Start the API
    app.run(debug=True)

    # Stop the facial recognition loop when the API is terminated
    face_thread.join()
