
# Virtual Air Painting with Hand Gestures 🎨✋

This Python project allows users to paint on a virtual canvas using only their index finger and a webcam. Leveraging **MediaPipe** for real-time hand tracking and **OpenCV** for image processing, the app enables gesture-based painting—no touchscreen or mouse needed.

## 🖼️ Features

- **Real-Time Hand Tracking:** Uses MediaPipe to track your hand and detect index finger position.
- **Virtual Canvas:** Paint on a transparent canvas over your webcam feed.
- **Color & Tool Switching:**
  - Press `r` for Red brush 🟥
  - Press `g` for Green brush 🟩
  - Press `b` for Blue brush 🟦
  - Press `e` to use the Eraser
  - Press `c` to Clear the Canvas
- **Custom Brush Thickness:** Adjustable brush and eraser sizes.
- **Natural Selfie Mode:** Webcam feed is flipped for intuitive use.

## 🛠️ Requirements

Install the required Python libraries using:

```bash
pip install opencv-python mediapipe numpy
```

## ▶️ How It Works

1. **Initialize Webcam:** Captures frames using OpenCV.
2. **Hand Detection:** MediaPipe detects hand landmarks in each frame.
3. **Finger Tracking:** The tip of the index finger is tracked in real-time.
4. **Drawing Logic:**
   - If the eraser tool is selected, it clears parts of the canvas.
   - Otherwise, colored circles are drawn where your finger moves.
5. **Keyboard Controls:** Easily switch between tools and colors using your keyboard.

## 💻 How to Run

1. Ensure your webcam is connected.
2. Run the Python script:

```bash
python air_painting.py
```

3. Use the following keys during execution:
   - `r`: Red Brush
   - `g`: Green Brush
   - `b`: Blue Brush
   - `e`: Eraser
   - `c`: Clear canvas
   - `q`: Quit the application

## 📁 File Overview

- `air_painting.py` — Main script that runs the virtual paint application.
- No additional configuration files are required.

## 📸 Example Output

> 👆 A webcam window appears where you draw in the air, and a semi-transparent painting trail follows your index finger.

## 📌 Notes

- **Performance Tip:** Ensure good lighting and keep your hand fully visible to the camera for best accuracy.
- The current setup supports one hand at a time and is optimized for basic drawing.

## 🧠 Future Improvements

- Add GUI-based color selection.
- Recognize more gestures (e.g., open palm to clear).
- Save your artwork with a hotkey.
