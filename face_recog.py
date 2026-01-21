
import face_recognition

def load_known_faces(image_paths):
    known_face_encodings = []
    known_face_names = []

    for name, path in image_paths.items():
        image = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(image)[0]

        known_face_encodings.append(encoding)
        known_face_names.append(name)

    return known_face_encodings, known_face_names


def recognize_faces(frame, known_face_encodings, known_face_names):
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    return face_locations, face_names
