import cv2
import face_recognition


KNOWN_IMAGES = {
    "Shreya": "images/Shreya.jpg",
    "Satish": "images/Satish.jpg",
    "Samyak": "images/Samyak.jpg"
}



def load_faces():
    known_face_encodings = []
    known_face_names = []

    for name, path in KNOWN_IMAGES.items():
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(name)
        else:
            print(f"No face found in {path}")

    return known_face_encodings, known_face_names


def detect_faces(frame, known_face_encodings, known_face_names):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    return face_locations, face_names


def draw_faces(frame, face_locations, face_names):
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_DUPLEX,
            0.5,
            (0, 0, 255),
            1
        )

    return frame