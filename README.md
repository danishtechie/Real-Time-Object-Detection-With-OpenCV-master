 Real-Time Object Detection Using YOLOv8
 By: Danish Maqbool Baig

Project Overview
This project implements a real-time object detection system using the YOLOv8 (You Only Look Once) model and the Flask framework. It utilizes a live webcam feed to detect and classify objects, displaying the results directly in a web browser with bounding boxes and confidence scores.

Features
Real-Time Detection: Detects multiple objects live through webcam input.
High Accuracy: Powered by YOLOv8, a state-of-the-art object detection algorithm.
Web Interface: Access the application through a user-friendly browser-based interface.
Confidence Filtering: Displays only objects with confidence levels above 30% (adjustable).
Performance Metrics: Displays FPS (Frames Per Second) to monitor system performance.
Stylish UI: Features a responsive design with gradient effects and animated buttons.

Demo Video/GIF (Optional)
Add a demo video or GIF showing the real-time detection feature in action.

Technologies Used
Programming Language: Python
Framework: Flask
Machine Learning Library: Ultralytics YOLOv8
Image Processing: OpenCV
Utility Library: Imutils

Folder Structure
php
Copy code
Fake_News_Detection/
├── static/                        # Static files (CSS/JS if added later)
├── templates/
│   └── index.html                 # HTML interface for the app
├── models/                        # Store trained models here (optional)
│   └── yolov8s.pt                 # YOLOv8 pre-trained model
├── app.py                         # Main Flask application
├── requirements.txt               # Required libraries
├── README.md                      # Documentation (This file)

Setup Instructions
1. Prerequisites
Python 3.x installed
Internet connection to download dependencies
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the Application
bash
Copy code
python app.py
4. Open in Browser
Navigate to the following URL in your browser:

arduino
Copy code
http://127.0.0.1:5000/

5. Usage
Click "Start Detecting" to activate the webcam and begin detection.
Click "Stop Detecting" to stop the camera feed and release the webcam.

Requirements File (requirements.txt)

Copy code:
flask
ultralytics
opencv-python
imutils


Customization
Change Confidence Threshold:
Open app.py and locate this line inside the generate_frames() function:
python
Copy code
if confidence > 0.3:  # Display only objects with confidence > 30%
Modify 0.3 to adjust the confidence threshold as needed.

Resize Frame Resolution for Faster Processing:
Locate this line in app.py:
python
Copy code
frame = cv2.resize(frame, (640, 480))  # Resize to 640x480
Change the resolution if required (e.g., (320, 240) for faster but lower quality processing).

Model Information
YOLOv8s: Lightweight and fast version of the YOLO model.
File Used: yolov8s.pt (pre-trained weights).

To improve accuracy, replace it with a larger model, such as yolov8m.pt or yolov8l.pt.
Performance Metrics
Displays FPS (Frames Per Second) to track real-time processing speed.
Prints elapsed time and FPS in the console upon stopping the detection.

Troubleshooting
1. Camera Not Opening?
Ensure the webcam is not being used by another application.
Replace the webcam index in this line if using an external camera:
python
Copy code
camera = cv2.VideoCapture(0)  # Change 0 to 1 for external camera

2. Module Not Found Errors?
Reinstall dependencies:
bash
Copy code
pip install -r requirements.txt

3. Performance Issues?
Reduce resolution:
python
Copy code
frame = cv2.resize(frame, (320, 240))  # Lower resolution for faster processing
Use a smaller YOLO model like yolov8n.pt.

To Add Features in the Future
Confidence Score Display Overlay: Highlight higher confidence detections with different colors.
Custom Object Detection: Train YOLOv8 on custom datasets using LabelImg for annotation.

Deploy as Web App: Host the application on platforms like Heroku or Render.
Speech-to-Text Integration: Announce detected objects using Python’s gTTS module.
License
This project is licensed under the MIT License.

Developer Information
Name: Danish Maqbool Baig
Email: [danishannu1111@gmail.com] 
Location: Baramulla, Kashmir
 

