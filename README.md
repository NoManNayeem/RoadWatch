
# RoadWatch - Traffic Monitoring System

**Repository URL**: [RoadWatch on GitHub](https://github.com/NoManNayeem/RoadWatch.git)

## Overview
RoadWatch is a traffic monitoring system built with Flask and YOLOv8 for real-time vehicle detection and traffic analysis. The app allows users to view live video feeds or demo traffic footage, displaying dynamic statistics on vehicle counts, types (cars, trucks, motorcycles), speed data, and more.

## Features
- **Live Camera Mode**: Tracks objects from a live video feed and displays real-time object statistics.
- **Demo Traffic Video Mode**: Processes a pre-recorded traffic video, showing detailed stats, including:
  - Vehicle counts for cars, trucks, and motorcycles.
  - Speed data (max, min, and average).
  - Vehicle colors and sample license plate data.

## Project Structure
```
RoadWatch/
├── app.py                   # Main application file
├── config.py                # Configuration settings
├── requirements.txt         # Dependencies
├── static/
│   └── css/
│       └── styles.css       # Custom styles
├── templates/
│   └── index.html           # Main HTML template
├── models/                  # Model files (YOLOv8)
├── videos/                  # Demo video files
└── README.md                # Project documentation
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NoManNayeem/RoadWatch.git
   cd RoadWatch
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the YOLOv8 model** (if not already included):
   Place the YOLO model (`yolov8n.pt`) in the `models/` folder.

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Open the app**:
   Visit `http://127.0.0.1:5000` in your browser.

3. **Choose video source**:
   - **Live Camera**: Tracks live feed with basic object stats.
   - **Demo Traffic Video**: Displays detailed traffic stats for cars, trucks, motorcycles, and speed data.

## Customization
- **Styles**: Edit `styles.css` in `static/css` to adjust the UI.
- **Configuration**: Adjust paths in `config.py` as needed.

## Dependencies
- Flask
- Ultralytics YOLOv8
- OpenCV

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

**Developed by**: NoManNayeem
