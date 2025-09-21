from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

def gen_frames():
    faceCascade = cv2.CascadeClassifier('/home/pi/Downloads/opencv-4.5.1/data/haarcascades/haarcascade_frontalcatface.xml')
    cap = cv2.VideoCapture(0)
    cap.set(3,640); cap.set(4,480)

    while True:
        ok, frame = cap.read()
        if not ok:
            continue
        frame = cv2.flip(frame, -1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20,20))
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\\r\\n'
               b'Content-Type: image/jpeg\\r\\n\\r\\n' + frame + b'\\r\\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
