import threading, time, queue, signal, sys
from .motor import MotorController
from .vision import VisionState, VisionWorker
from .bt_server import BTServer
from .config import FusionConf
from . import modes

CMD_WAIT=100; CMD_STOP=0; CMD_AUTO1=1; CMD_AUTO2=2; CMD_AUTO3=8; CMD_MANUAL=3
CMD_FWD=4; CMD_LEFT=5; CMD_BACK=6; CMD_RIGHT=7

def main():
    mc = MotorController()
    vs = VisionState()
    vw = VisionWorker(vs)
    cmd_queue = queue.Queue()
    bt = BTServer(cmd_queue)
    current = CMD_WAIT
    running = True

    vw.start()
    bt.start()

    def shutdown(*_):
        nonlocal running
        running = False
    signal.signal(signal.SIGINT, shutdown)

    print("[MAIN] Waiting for BT commands...")
    try:
        while running:
            # 최신 명령 흡수
            try:
                while True:
                    current = cmd_queue.get_nowait()
            except queue.Empty:
                pass

            if current == CMD_MANUAL:
                # 수동: 한 번의 세부 명령(4~7) 처리 후 정지
                try:
                    b = cmd_queue.get_nowait()
                except queue.Empty:
                    b = None

                if b == CMD_FWD:
                    mc.forward(100); time.sleep(0.5); mc.stop()
                elif b == CMD_LEFT:
                    mc.turn_left(70); time.sleep(0.2); mc.stop()
                elif b == CMD_BACK:
                    mc.backward(100); time.sleep(0.5); mc.stop()
                elif b == CMD_RIGHT:
                    mc.turn_right(70); time.sleep(0.2); mc.stop()
                else:
                    mc.stop()

            elif current == CMD_STOP:
                mc.stop(); time.sleep(0.05)

            elif current == CMD_AUTO1:
                with vs.lock: area = vs.face_area
                modes.mode_A1(mc, area, FusionConf()); time.sleep(0.05)

            elif current == CMD_AUTO2:
                with vs.lock: area = vs.face_area
                if area == 0: modes.mode_B1(mc)
                else:         modes.mode_B2(mc)
                time.sleep(0.05)

            elif current == CMD_AUTO3:
                with vs.lock: area = vs.face_area
                if area == 0: modes.mode_B1(mc)
                else:         modes.mode_C1(mc)
                time.sleep(0.05)

            else:
                mc.stop(); time.sleep(0.1)

    finally:
        print("[MAIN] shutdown")
        try: vw.stop()
        except: pass
        try: bt.stop()
        except: pass
        try: mc.cleanup()
        except: pass
        sys.exit(0)

if __name__ == "__main__":
    main()
