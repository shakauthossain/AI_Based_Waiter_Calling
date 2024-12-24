import cv2

def define_zones(frame):
    zones = []
    current_zone = []
    employee_names = []
    temp_coords = None  # Temporary variable to store coordinates for drawing
    input_box = ""  # Temporary string for employee name input
    is_typing = False  # Flag to indicate if we're typing a name

    def select_zone(event, x, y, flags, param):
        nonlocal current_zone, zones, temp_coords, is_typing, input_box

        # Left-click to start and complete a zone
        if event == cv2.EVENT_LBUTTONDOWN and not is_typing:
            if len(current_zone) == 0:
                current_zone.append((x, y))  # Start point
                print(f"Zone start: {current_zone[0]}")
            else:
                current_zone.append((x, y))  # End point
                temp_coords = None  # Clear temporary coordinates
                is_typing = True  # Start typing the employee name

        # Right-click to cancel the current zone
        elif event == cv2.EVENT_RBUTTONDOWN:
            print("Zone creation cancelled.")
            current_zone = []
            temp_coords = None

        # Update temporary coordinates for dynamic drawing
        elif event == cv2.EVENT_MOUSEMOVE and len(current_zone) == 1:
            temp_coords = (x, y)

    # Display the frame and set mouse callback
    print("Left-click to select the top-left and bottom-right corners of the zone.")
    print("Right-click to cancel the current zone.")
    cv2.namedWindow("Define Zones")
    cv2.setMouseCallback("Define Zones", select_zone)

    while True:
        temp_frame = frame.copy()

        # Draw the current zone (temporary rectangle)
        if len(current_zone) == 1 and temp_coords:
            cv2.rectangle(temp_frame, current_zone[0], temp_coords, (0, 255, 0), 2)

        # Draw all completed zones
        for i, zone in enumerate(zones):
            cv2.rectangle(temp_frame, zone[0], zone[1], (255, 0, 0), 2)
            cv2.putText(temp_frame, employee_names[i], (zone[0][0], zone[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        # Show input box if typing name
        if is_typing:
            cv2.rectangle(temp_frame, (50, 50), (450, 100), (255, 255, 255), -1)  # Background for input box
            cv2.rectangle(temp_frame, (50, 50), (450, 100), (0, 0, 0), 2)  # Border for input box
            cv2.putText(temp_frame, "Enter Name: " + input_box, (60, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        # Show the updated frame
        cv2.imshow("Define Zones", temp_frame)

        # Key press handling
        key = cv2.waitKey(1) & 0xFF

        # Handle typing input
        if is_typing:
            if key == 8:  # Backspace
                input_box = input_box[:-1]
            elif key == 13:  # Enter key
                if input_box.strip():
                    employee_names.append(input_box.strip())
                    zones.append(tuple(current_zone))
                    print(f"Zone {len(zones)}: {current_zone} assigned to {input_box.strip()}")
                else:
                    print("Empty name! Please enter a valid name.")
                input_box = ""
                current_zone = []
                is_typing = False
            elif key != 255:  # Ignore invalid keys
                input_box += chr(key)

        # Exit on pressing 'q'
        if key == ord('q') and not is_typing:
            break

    cv2.destroyAllWindows()
    return zones, employee_names