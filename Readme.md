# Gesture-Based Mouse Control

This Python project allows users to control their computer's mouse pointer and simulate clicks using hand gestures captured by a webcam. It leverages state-of-the-art libraries, including **MediaPipe** for hand tracking, **OpenCV** for video capture, **PyAutoGUI** for simulating mouse actions, and **Pynput** for controlling the mouse.

By recognizing specific hand gestures, users can move the mouse cursor, left-click, right-click, and even double-click—all without touching a physical mouse.

## Features

- **Real-time Mouse Movement**: The script tracks the **index finger tip**'s position in real time and moves the mouse cursor accordingly.
- **Gesture-Based Control**: Three main mouse actions are detected based on hand gestures:
  - **Left Click**: Triggered by a specific gesture (thumb and index finger form a specific angle).
  - **Right Click**: Triggered by a different gesture with the thumb and index finger.
  - **Double Click**: Triggered by a gesture with the thumb and index finger positioned close together.
- **Exponential Smoothing**: Smooths mouse movement by applying exponential smoothing to reduce jitter and make the mouse movements more natural and stable.
- **Real-Time Hand Tracking**: Detects and tracks hand landmarks in real time using **MediaPipe**.

## Requirements

Before running the script, you must install the following dependencies. You can install them via **pip**:

- **OpenCV**: For video capture and image processing.
- **MediaPipe**: For hand tracking and gesture detection.
- **PyAutoGUI**: For simulating mouse actions such as clicking and double-clicking.
- **Pynput**: For controlling the mouse using the `pynput.mouse.Controller`.

To install these libraries, run the following command:

```bash
pip install opencv-python mediapipe pyautogui pynput
```

## How It Works

1. **Webcam Capture:** The script opens the webcam feed using OpenCV and captures each frame for processing.
2. **Hand Landmark Detection:** The MediaPipe library detects key landmarks (points) on the hand, such as the positions of the fingers and palm.
3. **Mouse Movement:** The position of the index finger tip is mapped to the screen coordinates, allowing the user to move the mouse cursor by simply moving their finger.
4. **Gesture Recognition:** The script detects predefined hand gestures based on the angles and distances between specific fingers:
    - **Left Click Gesture:** The hand forms a particular shape where the thumb and index finger create a specific angle.
    - **Right Click Gesture:** A different hand posture triggers a right-click.
    - **Double Click Gesture:** A gesture where the thumb and index finger are close together simulates a double-click action.
5. **Smoothing:** To ensure smooth and stable cursor movement, exponential smoothing is applied to the cursor’s position, reducing jitter.

## How to Run

### 1. Set Up Dependencies

Ensure that the required libraries are installed using the following command:

```bash
pip install opencv-python mediapipe pyautogui pynput
```
### 2. Run the Script
To start the program, simply execute the script:

```bash
python gesture_mouse_control.py
```
### 3. Interact with the Program
Once the script is running, the webcam feed will open, and you’ll see a live feed of your hand. The following gestures will trigger different actions:

- **Move the Mouse:** Move your index finger tip to move the mouse cursor in real-time.
- **Left Click:** Make a specific hand gesture with your thumb and index finger (e.g., a certain angle between them).
- **Right Click:** Perform another predefined gesture with the thumb and index finger.
- **Double Click:** Bring the thumb and index finger together to simulate a double-click.
### 4. Exit the Program
To exit the program and close the webcam feed, press the ```q``` key.

