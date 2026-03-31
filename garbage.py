from ultralytics import YOLO


def load_model(model_path):
    model = YOLO(model_path)
    return model


def detect_garbage(model, frame):
    results = model(frame)
    garbage_detected = False

    annotated_frame = results[0].plot()

    for result in results:
        if len(result.boxes) > 0:
            garbage_detected = True
            break

    return garbage_detected, annotated_frame