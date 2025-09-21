# mungchi-capstone-3-1

## Third-Party Licenses
이 프로젝트는 다음 오픈소스 라이브러리를 사용하며, 각 라이브러리는 자체 라이선스를 따릅니다.

- [OpenCV](https://opencv.org/) – **Apache License 2.0**
- [PyBluez](https://github.com/pybluez/pybluez) – **GPL-2.0-or-later**
- [imutils](https://github.com/jrosebr1/imutils) – **MIT License**


## System Overview
![System Diagram](System%20Diagram.png)

## Circuit Wiring
![Circuit Diagram](Circuit%20Diagram.png)
 3.6V 3500mA 스펙의 리튬배터리 4개와 TP4056 충전 모듈 4개를 이용.
· TP 4056 입력단을 병렬로 연결하여 한 포트 연결 시 전체 배터리 충전.
(유, 무선 충전 지원)
· 2개의 TP 4056 출력단 OUTPUT과 BAT 단자를 연결하여 7.2V 전압 출력

· L298 -> 7.2V 구동
· 라즈베리파이 -> 감압기를 통해 4.8V 구동

## Mobile App UI
![App Screen](App%20Screen.png)
![App Screen explain](App%20Screen%20explain.png)
