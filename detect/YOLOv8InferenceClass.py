
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

import cv2

model = YOLO("yolov8l.pt")

results = model.predict(source="PETS09-S2L2-raw.mp4",show=True)
print(results)