
from ultralytics import YOLO

def load_yolo_model(model_path):
    return YOLO(model_path)

def detect_objects(model, frame):
    results = model(frame)
    frame_with_results = results[0].plot()
    return frame_with_results
