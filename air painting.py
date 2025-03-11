import cv2
import numpy as np
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

# Colors and Brush Thickness
brush_thickness = 15
eraser_thickness = 50
draw_color = (255, 0, 0)  # Default color: Blue

# Canvas to draw
canvas = None

# Function to detect hand landmarks and return tip position of index finger
def get_index_finger_position(results, img_width, img_height):
    for hand_landmarks in results.multi_hand_landmarks:
        index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        return int(index_finger_tip.x * img_width), int(index_finger_tip.y * img_height)
    return None

# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame horizontally for a natural selfie view
    frame = cv2.flip(frame, 1)
    img_height, img_width, _ = frame.shape

    # Create canvas if not initialized
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        # Get index finger position
        finger_position = get_index_finger_position(results, img_width, img_height)
        
        if finger_position:
            x, y = finger_position

            # Detect gestures based on position or logic (for simplicity, no menu here)
            # Draw a circle at the tip for visualization
            cv2.circle(frame, (x, y), 10, draw_color, -1)

            # Draw on canvas
            if draw_color != (0, 0, 0):  # Not erasing
                cv2.circle(canvas, (x, y), brush_thickness, draw_color, -1)
            else:  # Eraser
                cv2.circle(canvas, (x, y), eraser_thickness, (0, 0, 0), -1)

    # Combine frame and canvas
    combined = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    # Display the video stream
    cv2.imshow('Virtual Air Painting Canvas', combined)

    # Check for key presses
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Quit
        break
    elif key == ord('c'):  # Clear canvas
        canvas = np.zeros_like(frame)
    elif key == ord('r'):  # Red color
        draw_color = (0, 0, 255)
    elif key == ord('g'):  # Green color
        draw_color = (0, 255, 0)
    elif key == ord('b'):  # Blue color
        draw_color = (255, 0, 0)
    elif key == ord('e'):  # Eraser
        draw_color = (0, 0, 0)

# Release the resources
cap.release()
cv2.destroyAllWindows()
