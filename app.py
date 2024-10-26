from flask import Flask, render_template, Response, request, jsonify
from ultralytics import YOLO
import cv2
import time
import json
import random
import config
import os

app = Flask(__name__)
model = YOLO(config.YOLO_MODEL_PATH)

# Generate frames and process them for the live or demo video feed
def generate_frames(source=0):
    cap = cv2.VideoCapture(source)
    while True:
        success, frame = cap.read()
        if not success:
            break
        results = model(frame)
        frame = process_frame(frame, results)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()

# Process frame and update stats based on source type (live or demo)
def process_frame(frame, results):
    stats = {
        "vehicle_count": len(results[0].boxes),
        "max_speed": random.randint(50, 100),
        "min_speed": random.randint(20, 50),
        "avg_speed": random.randint(35, 80),
        "colors": ["Red", "Blue", "Black"],
        "number_plates": [f"ABC{random.randint(100,999)}"]
    }
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = box.conf[0]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{confidence:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    return frame

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    source_type = request.args.get("source", "camera")
    source = 0 if source_type == "camera" else os.path.join(config.VIDEO_DIR, "demo_video.mp4")
    return Response(generate_frames(source), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/stats_feed")
def stats_feed():
    source_type = request.args.get("source", "camera")
    demo_mode = source_type == "video"
    
    def generate_stats():
        while True:
            if demo_mode:
                # Demo statistics for traffic data
                stats = {
                    "vehicle_count": random.randint(10, 30),
                    "car_count": random.randint(5, 15),
                    "truck_count": random.randint(1, 5),
                    "motorcycle_count": random.randint(0, 5),
                    "max_speed": random.randint(60, 120),
                    "min_speed": random.randint(20, 40),
                    "avg_speed": random.randint(40, 80),
                    "colors": ["Red", "Blue", "Black", "White", "Green"],
                    "number_plates": [f"XYZ{random.randint(100,999)}" for _ in range(5)]
                }
            else:
                # Live statistics for generic tracking
                stats = {
                    "tracked_objects": random.choice(["Person", "Vehicle", "Object"]),
                    "count": random.randint(1, 5),
                    "detection_confidence": random.randint(50, 100)
                }
            yield f"data: {json.dumps(stats)}\n\n"
            time.sleep(1)

    return Response(generate_stats(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
