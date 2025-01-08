from flask import Flask, render_template, Response
from ultralytics import YOLO
import cv2
import time
from imutils.video import FPS

# Initialize Flask app
app = Flask(__name__)

# Load YOLOv8 model (Switch to a more accurate model if needed)
model = YOLO("yolov8s.pt")  # 'yolov8s.pt' for better accuracy

# Initialize webcam
camera = cv2.VideoCapture(0)  # 0 for default webcam

# Start FPS counter
fps = FPS().start()


def generate_frames():
    """
    Capture frames from the webcam and process them for real-time detection.
    """
    while True:
        success, frame = camera.read()  # Capture frame from webcam
        if not success:
            break

        # Resize frame for faster processing
        frame = cv2.resize(frame, (640, 480))  # Resize to 640x480

        # Perform object detection
        results = model(frame)

        # Draw bounding boxes and labels
        for result in results:
            for box in result.boxes:
                # Extract coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Confidence filtering (adjust threshold here)
                confidence = box.conf[0]
                if confidence > 0.3:  # Display only objects with confidence > 0.3
                    label = f"{result.names[int(box.cls[0])]}: {confidence:.2f}"

                    # Draw rectangle and label
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Encode frame
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Update FPS counter
        fps.update()

        # Yield the frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    """
    Render the index.html page.
    """
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    """
    Stream video feed to the browser.
    """
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stop_camera')
def stop_camera():
    """
    Stop the camera feed and release the webcam.
    """
    global camera
    if camera.isOpened():  # Release the camera
        camera.release()  # Properly releases the webcam
    cv2.destroyAllWindows()  # Close OpenCV windows

    # Stop FPS counter and show stats
    fps.stop()
    print(f"[INFO] Elapsed Time: {fps.elapsed():.2f} seconds")
    print(f"[INFO] Approximate FPS: {fps.fps():.2f}")

    return "Camera released successfully"


if __name__ == '__main__':
    app.run(debug=True)
