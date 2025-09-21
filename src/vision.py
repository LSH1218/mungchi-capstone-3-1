import cv2
import threading
from .config import VisionConf

class VisionState:
    def __init__(self):
        self.face_area = 0
        self.face_center = (0, 0)
        self.face_found = False
        self.lock = threading.Lock()

class VisionWorker(threading.Thread):
    """
    카메라에서 프레임 읽고 고양이 얼굴 검출 → face_area/center 상태 갱신
    """
    def __init__(self, state: VisionState, conf: VisionConf = VisionConf()):
        super().__init__(daemon=True)
        self.state = state
        self.conf = conf
        self._stop = threading.Event()

    def run(self):
        faceCascade = cv2.CascadeClassifier(self.conf.cascade_path)
        cap = cv2.VideoCapture(self.conf.cam_index)
        cap.set(3, self.conf.frame_width)
        cap.set(4, self.conf.frame_height)
        while not self._stop.is_set():
            ok, frame = cap.read()
            if not ok:
                continue
            frame = cv2.flip(frame, -1)  # 필요 없으면 제거
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=self.conf.scaleFactor,
                minNeighbors=self.conf.minNeighbors,
                minSize=self.conf.minSize
            )
            if len(faces) > 0:
                (x,y,w,h) = faces[0]
                area = int(w*h)
                center = (int(x + w/2), int(y + h/2))
                with self.state.lock:
                    self.state.face_area = area
                    self.state.face_center = center
                    self.state.face_found = True
            else:
                with self.state.lock:
                    self.state.face_area = 0
                    self.state.face_found = False
        cap.release()

    def stop(self):
        self._stop.set()
