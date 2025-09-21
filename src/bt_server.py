import threading, time, queue

try:
    import bluetooth  # PyBluez
    _BT_AVAILABLE = True
except Exception:
    _BT_AVAILABLE = False

class BTServer(threading.Thread):
    """
    RFCOMM 서버: 수신 바이트 → 정수 명령으로 파싱 → out_queue로 put
    """
    def __init__(self, out_queue: queue.Queue, port:int=1):
        super().__init__(daemon=True)
        self.q = out_queue
        self.port = port
        self._stop = threading.Event()

    def run(self):
        if not _BT_AVAILABLE:
            print("[WARN] PyBluez 없음 → BTServer는 대기만 합니다.")
            while not self._stop.is_set():
                time.sleep(1.0)
            return

        server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_socket.bind(("", self.port))
        server_socket.listen(1)
        client_socket, address = server_socket.accept()
        print("[BT] connected:", address)
        try:
            client_socket.send(b"hello")
        except: pass

        try:
            while not self._stop.is_set():
                data = client_socket.recv(1024)
                if not data:
                    continue
                try:
                    val = int(data.decode().strip())
                    self.q.put(val)
                except Exception:
                    continue
        finally:
            try: client_socket.close()
            except: pass
            server_socket.close()

    def stop(self):
        self._stop.set()
