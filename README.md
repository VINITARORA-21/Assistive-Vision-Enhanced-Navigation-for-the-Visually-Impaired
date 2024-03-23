# Assistive-Vision-Enhanced-Navigation-for-the-Visually-Impaired
This project implements a pedestrian safety system using the YOLO (You Only Look Once) object detection algorithm, OpenCV for video processing, gTTS (Google Text-to-Speech) for audio feedback, and Ultralytics for easy integration of YOLO models.

## Overview
The system detects pedestrians and crosswalks in real-time using a webcam feed. When a pedestrian approaches a crosswalk and a green light is detected, the system provides an audio alert indicating that it's safe to cross the road

## Components
1. YOLOv8 Model
The YOLOv8 model is used for real-time object detection. It is pre-trained to detect pedestrians and traffic lights (specifically, green lights).

2. OpenCV
OpenCV is used for capturing video from the webcam, processing frames, and displaying annotated frames with detected objects.

3. gTTS (Google Text-to-Speech)
gTTS is used to convert text alerts into spoken audio. Alerts are triggered when a pedestrian is detected near a crosswalk and a green light is detected.

4. Ultralytics
Ultralytics provides an easy-to-use interface for working with YOLO models in PyTorch. It simplifies model loading, inference, and result visualization.

## Usage
* Ensure that your webcam is connected and accessible by OpenCV.

* Run the pedestrian_safety_system.py script.

* Point the webcam towards an area with pedestrians and crosswalks.

* When a pedestrian approaches a crosswalk and a green light is detected, the system will provide an audio alert.

* Press 'q' to exit the application.

## High-End Computing Device
The YOLO model was trained and fine-tuned on a high-end computing device with the following specifications:

* GPU: NVIDIA Quadro GP100 and Quadro P400
* CUDA Version: 12.2
* Driver Version: 535.104.12
* Memory: 16GB (GP100), 2GB (P400)
* The high-end computing device provided significant computational power for training and fine-tuning the YOLO model, enabling efficient object detection in real- 
time applications.


## Acknowledgements
* YOLOv8 model: Ultralytics YOLO
* gTTS: gTTS GitHub
* OpenCV: OpenCV
