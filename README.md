# mungchi-capstone-3-1

## Third-Party Licenses
이 프로젝트는 다음 오픈소스 라이브러리를 사용하며, 각 라이브러리는 자체 라이선스를 따릅니다.

- [OpenCV](https://opencv.org/) – **Apache License 2.0**
- [PyBluez](https://github.com/pybluez/pybluez) – **GPL-2.0-or-later**
- [imutils](https://github.com/jrosebr1/imutils) – **MIT License**


## System Overview
![System Diagram](System%20Diagram.png)

스마트폰 → 블루투스 → 라즈베리파이 → 모터 드라이버(L298) → DC모터로 이어지는 제어 흐름을 보여준다.  
라즈베리파이 카메라는 고양이 얼굴을 실시간 인식하여 자동 주행 모드에서 모터 제어에 반영한다.  
무선 충전 모듈과 배터리 팩을 통해 완전 무선으로 동작이 가능하다.


## Circuit Wiring
![Circuit Diagram](Circuit%20Diagram.png)

· 3.6V 3500mA 스펙의 리튬배터리 4개와 TP4056 충전 모듈 4개를 이용한다.
· TP 4056 입력단을 병렬로 연결하여 한 포트 연결 시 전체 배터리 충전한다.
(유, 무선 충전 지원)
· 2개의 TP 4056 출력단 OUTPUT과 BAT 단자를 연결하여 7.2V 전압 출력

· L298 -> 7.2V 구동
· 라즈베리파이 -> 감압기를 통해 4.8V 구동

## Mobile App UI
![App Screen](App%20Screen.png)
![App Screen explain](App%20Screen%20explain.png)


앱에서 블루투스 연결 및 영상 스트리밍 주소(IP)를 설정하고 주행 모드를 선택할 수 있다.  
· 자동주행1~3 : 고양이 얼굴을 인식해 거리·위치에 따라 모터를 제어  
· 수동주행 : 전/후/좌/우 버튼으로 직접 주행  
· 정지 버튼 : 모든 동작을 즉시 중지

