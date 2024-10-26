import os

# YOLO Model Path
YOLO_MODEL_PATH = "models/yolov8n.pt"

# Directory Paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VIDEO_DIR = os.path.join(BASE_DIR, "videos")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Flask Settings
DEBUG = True
