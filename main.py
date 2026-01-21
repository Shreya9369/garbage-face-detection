
import cv2
from config import (
    ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER,
    CONTACT_NUMBERS, IMAGE_PATHS, YOLO_MODEL_PATH, CAMERA_INDEX
)
from face_recog import load_known_faces, recognize_faces
from yolo_detect import load_yolo_model, detect_objects
from alert_twilio import TwilioAlert


def main():

    # Load YOLO model
    model = load_yolo_model(YOLO_MODEL_PATH)

    # Load known faces (same as your logic)
    known_face_encodings, known_face_names = load_known_faces(IMAGE_PATHS)

    # Twilio client
    alert = TwilioAlert(ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, CONTACT_NUMBERS)

    # Open webcam
    cap = cv2.VideoCapture(CAMERA_INDEX)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO Detection
        frame_with_yolo_results = detect_objects(model, frame)

        # Face Recognition
        face_locations, face_names = recognize_faces(
            frame, known_face_encodings, known_face_names
        )

        # Draw boxes + send alerts
        for (top, right, bottom, left), name in zip(face_locations, face_names):

            cv2.rectangle(frame_with_yolo_results, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame_with_yolo_results, name, (left, top - 10),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 1)

            alert.send_alert_if_needed(name)

        cv2.imshow("YOLOv8 + Face Recognition", frame_with_yolo_results)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
