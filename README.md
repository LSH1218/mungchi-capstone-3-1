# mungchi-capstone-3-1

## Third-Party Licenses
이 프로젝트는 다음 오픈소스 라이브러리를 사용하며, 각 라이브러리는 자체 라이선스를 따릅니다.

- [OpenCV](https://opencv.org/) – **Apache License 2.0**
- [PyBluez](https://github.com/pybluez/pybluez) – **GPL-2.0-or-later**
- [imutils](https://github.com/jrosebr1/imutils) – **MIT License**


## System Overview
![System Diagram](<img width="587" height="331" alt="image" src="https://github.com/user-attachments/assets/211c4011-e9a9-4b6b-995a-f327ec89d197" />
)

## Circuit Wiring
![Circuit Diagram](<img width="580" height="341" alt="image" src="https://github.com/user-attachments/assets/6e4b9500-0235-4add-bfa8-58cb01652b71" />
)
 3.6V 3500mA 스펙의 리튬배터리 4개와 TP4056 충전 모듈 4개를 이용.
· TP 4056 입력단을 병렬로 연결하여 한 포트 연결 시 전체 배터리 충전.
(유, 무선 충전 지원)
· 2개의 TP 4056 출력단 OUTPUT과 BAT 단자를 연결하여 7.2V 전압 출력

· L298 -> 7.2V 구동
· 라즈베리파이 -> 감압기를 통해 4.8V 구동

## Mobile App UI
![App Screen](<img width="332" height="532" alt="image" src="https://github.com/user-attachments/assets/34a26391-4024-43d3-ae87-e5671c6d1bba" />
)
![App Screen explain](<img width="663" height="373" alt="image" src="https://github.com/user-attachments/assets/55ac1b34-a9d4-4370-9ff6-fdf932ba44ab" />
)
