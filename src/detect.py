from ultralytics import YOLO
import argparse
import os

parser = argparse.ArgumentParser(description="YOLO11n Object Detection")
parser.add_argument("--source", required=True, help="Path to image/video")
parser.add_argument("--conf", type=float, default=0.25)
args = parser.parse_args()

model_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "model",
    "best.pt"
)

model = YOLO(model_path)

results = model.predict(
    source=args.source,
    conf=args.conf,
    save=True
)

print("Detection completed successfully.")