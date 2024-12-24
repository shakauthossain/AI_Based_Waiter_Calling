import cv2
import time
from zone_selector import define_zones
from hand_detector import initialize_detector, process_hand_landmarks
from utilities import map_hand_to_employee
from notification import send_notification
import mediapipe as mp

def main(video_path=None):
    # Use webcam or video input
    if video_path:
        cap = cv2.VideoCapture(video_path)
    else:
        cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Read the first frame to define zones
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read video.")
        return

    # Define zones interactively
    zones, employee_names = define_zones(frame)
    print("Zones and employee names defined:", list(zip(employee_names, zones)))

    # Display the frame with marked zones
    for zone, name in zip(zones, employee_names):
        cv2.rectangle(frame, zone[0], zone[1], (0, 255, 0), 2)
        cv2.putText(frame, name, (zone[0][0], zone[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.imshow("Marked Zones", frame)
    print("Press 'r' to start video processing.")

    # Wait for 'r' key press to start video processing
    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == ord('r'):
            break

    cv2.destroyWindow("Marked Zones")

    # Initialize hand detector
    hands_detector, mp_hands = initialize_detector()

    # List to store employees requesting coffee along with timestamps
    coffee_requests = []

    # Process video frame by frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Use the process_hand_landmarks function from hand detection code
        processed_image = process_hand_landmarks(frame, hands_detector)

        # Convert frame to RGB for MediaPipe
        frame_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
        results = hands_detector.process(frame_rgb)

        frame_height, frame_width, _ = frame.shape

        if results.multi_hand_landmarks:  # Check if any hands are detected
            for hand_landmarks in results.multi_hand_landmarks:
                hand_x = int(hand_landmarks.landmark[0].x * frame_width)
                hand_y = int(hand_landmarks.landmark[0].y * frame_height)

                employee = map_hand_to_employee(hand_x, hand_y, zones, employee_names)
                if employee and employee not in [req['name'] for req in coffee_requests]:
                    print(f"{employee} has raised their hand for coffee!")
                    send_notification(employee)

                    # Add the employee to coffee_requests with current timestamp
                    coffee_requests.append({'name': employee, 'time': time.time()})

        # Check if any requests have expired (older than 5 seconds)
        current_time = time.time()
        coffee_requests = [req for req in coffee_requests if current_time - req['time'] <= 5]

        # Display all coffee requests
        y_offset = 50  # Initial vertical position for the text
        for request in coffee_requests:
            cv2.putText(frame, f"{request['name']} needs coffee", (50, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            y_offset += 40  # Increment vertical position for the next request

        cv2.imshow("Office View", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'desk_video.mp4'  # Replace with the actual video path or leave None for webcam
    main(video_path)
