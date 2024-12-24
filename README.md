# Hand Raised Coffee Request System

This project utilizes computer vision to detect when an employee raises their hand to request coffee. It tracks hand gestures using MediaPipe's hand tracking model and associates the requests with employees based on predefined zones in the video feed.

---

## Features

- **Hand Detection**: Detects raised hands using MediaPipe's hand tracking model.
- **Employee Identification**: Identifies employees based on their position in predefined zones in the video.
- **Coffee Requests**: Generates and displays a coffee request when an employee raises their hand.
- **Automatic Notifications**: Sends a notification to the designated person for each coffee request.
- **Request Expiry**: Automatically removes coffee requests after 5 seconds for a clean interface.
- **Dynamic Zone Definition**: Allows interactive definition of zones to adapt to different room layouts.

---

## Requirements

- **Python**: Version 3.6+
- **Libraries**:
  - OpenCV (`cv2`)
  - MediaPipe
  - NumPy
  - Other standard libraries (`time`, etc.)

Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file, you can manually install the necessary packages:

```bash
pip install opencv-python mediapipe numpy
```

---

## Usage

### Running the Application (Webcam)

To run the application using your webcam:

```bash
python main.py
```

### Running with a Video File

To process a video file instead of using the webcam, pass the video path as an argument:

```bash
python main.py --video_path "path/to/your/video.mp4"
```

---

## Key Features During Execution

- **Dynamic Zone Setup**: 
  - Use the mouse to interactively define zones on the video.
  - Assign specific zones to employees by clicking and dragging the mouse on the frame.

- **Key Commands**:
  - **Left Mouse Button**: Select and add a zone for a specific employee.
  - **Press "r"**: Start processing the video after defining the zones.
  - **Press "q"**: Quit the application at any time.

---

## Workflow

1. **Define Zones**: Interactively mark the zones for employees using the mouse on the video feed.
2. **Start Processing**: Press **"r"** to begin detecting hand gestures.
3. **Coffee Requests**:
   - If an employee raises their hand in their defined zone, a coffee request is generated.
   - The system displays the request and sends a notification.
4. **Automatic Removal**: Requests disappear after 5 seconds to prevent clutter.
5. **Quit**: Press **"q"** to exit the application.

---

## Customization

- **Zone Setup**: Zones can be redefined by modifying the logic for dynamic zone marking in the script.
- **Request Expiry**: Adjust the expiration time for coffee requests in the code.
- **Notification Logic**: Modify the notification mechanism to suit your requirements.

---

## Troubleshooting

- **Hand Detection Issues**:
  - Ensure the lighting is sufficient for the camera to detect hand gestures.
  - Adjust the camera angle for better visibility.
- **Zone Definition**:
  - If zones are not being defined correctly, recheck the zone marking logic or adjust the frame dimensions in the script.

---

## Contact

For questions or suggestions, contact **Shakaut Hossain** at [shakauthossain0@gmail.com](mailto:shakauthossain0@gmail.com).

---
