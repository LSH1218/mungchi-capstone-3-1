import time
from .config import Pins, PWMConf

try:
    import RPi.GPIO as GPIO
    _GPIO_AVAILABLE = True
except Exception:
    _GPIO_AVAILABLE = False

class MotorController:
    """
    IN1/IN2 = 왼쪽, IN3/IN4 = 오른쪽.
    예전 코드와 동일한 방향 매핑:
      - '전진'  : IN3=HIGH, IN4=LOW,  IN2=HIGH, IN1=LOW
      - '후진'  : IN4=HIGH, IN3=LOW,  IN1=HIGH, IN2=LOW
      - '좌회전': IN4=HIGH, IN3=LOW,  IN2=HIGH, IN1=LOW
      - '우회전': IN3=HIGH, IN4=LOW,  IN1=HIGH, IN2=LOW
    """
    def __init__(self, pins: Pins = Pins(), pwm: PWMConf = PWMConf()):
        self.pins = pins
        self.conf = pwm
        self._setup()

    def _setup(self):
        if not _GPIO_AVAILABLE:
            print("[WARN] RPi.GPIO not available → DRY-RUN")
            return
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for p in (self.pins.IN1, self.pins.IN2, self.pins.IN3, self.pins.IN4, self.pins.EN1, self.pins.EN2):
            GPIO.setup(p, GPIO.OUT)
        self.pwm_left = GPIO.PWM(self.pins.EN1, self.conf.freq_left)
        self.pwm_right = GPIO.PWM(self.pins.EN2, self.conf.freq_right)
        self.pwm_left.start(0)
        self.pwm_right.start(0)
        self.stop()

    def _write(self, in1, in2, in3, in4):
        if not _GPIO_AVAILABLE:
            return
        GPIO.output(self.pins.IN1, in1)
        GPIO.output(self.pins.IN2, in2)
        GPIO.output(self.pins.IN3, in3)
        GPIO.output(self.pins.IN4, in4)

    def _dc(self, left_dc, right_dc):
        left_dc = max(self.conf.min_dc, min(self.conf.max_dc, int(left_dc)))
        right_dc = max(self.conf.min_dc, min(self.conf.max_dc, int(right_dc)))
        if not _GPIO_AVAILABLE:
            print(f"[DRY] DC L/R = {left_dc}/{right_dc}")
            return
        self.pwm_left.ChangeDutyCycle(left_dc)
        self.pwm_right.ChangeDutyCycle(right_dc)

    def forward(self, dc=100):
        self._dc(dc, dc)
        self._write(0,1,1,0)  # IN1=LOW, IN2=HIGH / IN3=HIGH, IN4=LOW

    def backward(self, dc=100):
        self._dc(dc, dc)
        self._write(1,0,0,1)

    def turn_left(self, dc=60):
        self._dc(dc, dc)
        self._write(0,1,0,1)

    def turn_right(self, dc=60):
        self._dc(dc, dc)
        self._write(1,0,1,0)

    def stop(self):
        self._dc(0, 0)
        self._write(0,0,0,0)

    def cleanup(self):
        if not _GPIO_AVAILABLE:
            return
        try:
            self.pwm_left.stop()
            self.pwm_right.stop()
        finally:
            GPIO.cleanup()
