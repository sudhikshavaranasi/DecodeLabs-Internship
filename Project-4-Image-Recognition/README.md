# Project 4 - Object Detection Using OpenCV

## Objective
Develop a basic object detection system using Computer Vision techniques to identify faces in an image.

## Description
This project uses OpenCV's Haar Cascade Classifier to detect human faces in an image. Detected faces are highlighted using bounding boxes, demonstrating the fundamentals of object detection.

## Features
- Reads image input
- Detects faces automatically
- Draws bounding boxes around detected faces
- Displays the detection result visually
- Simple implementation using OpenCV

## Technologies Used
- Python
- OpenCV

## How It Works
1. Load an image.
2. Convert the image to grayscale.
3. Apply Haar Cascade face detection.
4. Identify face locations.
5. Draw rectangles around detected faces.
6. Display the final image.

## Requirements

```bash
pip install opencv-python
```

## Run the Program

```bash
python face_detection.py
```

## Output
The program displays the image with rectangles drawn around detected faces.

## Future Enhancements
- Detect multiple object categories
- Real-time webcam detection
- Integrate deep learning models
- Improve detection accuracy
