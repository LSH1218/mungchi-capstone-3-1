from dataclasses import dataclass

@dataclass
class Pins:
    IN1: int = 23  # 왼쪽 모터 전/후 (IN1/IN2)
    IN2: int = 24
    IN3: int = 26  # 오른쪽 모터 전/후 (IN3/IN4)
    IN4: int = 6
    EN1: int = 12  # 왼쪽 PWM
    EN2: int = 5   # 오른쪽 PWM

@dataclass
class PWMConf:
    freq_left: int = 500
    freq_right: int = 500
    min_dc: int = 0    # 0~100 사이에서 제어
    max_dc: int = 100

@dataclass
class VisionConf:
    cascade_path: str = "/home/pi/Downloads/opencv-4.5.1/data/haarcascades/haarcascade_frontalcatface.xml"
    cam_index: int = 0
    frame_width: int = 640
    frame_height: int = 480
    scaleFactor: float = 1.2
    minNeighbors: int = 5
    minSize: tuple = (20, 20)

@dataclass
class FusionConf:
    area_forward_threshold: int = 70000  # facescale 임계 (예전 코드 유지)
    area_scale_div: int = 700            # 듀티 계산 분모
