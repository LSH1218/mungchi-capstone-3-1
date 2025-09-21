from .config import FusionConf
from .motor import MotorController

def mode_A1(mc: MotorController, face_area:int, conf:FusionConf=FusionConf()):
    """
    facescale(면적)에 따라:
      0 → 우회전(탐색), 임계보다 작으면 전진, 크면 후진
    """
    th = conf.area_forward_threshold
    if face_area == 0:
        mc.turn_right(dc=30)
    elif face_area < th:
        duty = max(30, min(100, 100 - (face_area // conf.area_scale_div)))
        mc.forward(dc=duty)
    else:
        duty = max(30, min(100, (face_area // conf.area_scale_div) - 100))
        mc.backward(dc=duty)

def mode_B1(mc: MotorController):
    mc.turn_right(dc=20)

def mode_B2(mc: MotorController):
    mc.turn_right(dc=80)  # 강한 우회전

def mode_C1(mc: MotorController):
    mc.forward(dc=100)
