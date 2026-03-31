import cv2

from face_module.face import load_faces, detect_faces, draw_faces
from garbage_module.garbage import load_model, detect_garbage
from messaging_module.message import Messenger


MODEL_PATH = "models/best.pt"


def main():
    known_face_encodings, known_face_names = load_faces()
    garbage_model = load_model(MODEL_PATH)
    messenger = Messenger()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Could not read frame")
            break

        garbage_detected, annotated_frame = detect_garbage(garbage_model, frame)

        face_locations, face_names = detect_faces(frame, known_face_encodings, known_face_names)

        annotated_frame = draw_faces(annotated_frame, face_locations, face_names)

        if garbage_detected:
            for name in face_names:
                if name != "Unknown":
                    messenger.send(name)

        cv2.imshow("Garbage + Face Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()