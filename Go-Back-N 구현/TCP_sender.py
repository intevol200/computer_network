import socket
import time

'''
=== 송신자 ===
TCP 기반 GO-BACK-N 프로토콜 구현
20175288 최광삼
'''

HOST = '127.0.0.1' # IP, 포트 경로 지정
PORT = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP 소켓 설정
client_socket.connect((HOST, PORT)) # 소켓 경로 설정

print("[GO-BACK-N Protocol]")
print("----- Sender -----")

base = 0 # BASE 초기화
win_size = 5 # 보낼 패킷량
count = 0 # 순번 초기화

for a in range(base, win_size):
    if(a < 2): # 패킷 송신
        send1 = "pkt : " + str(a)
        count = count + 1
        print("   send pkt :", a)
        client_socket.sendall(send1.encode())

    elif(a == 2): # 패킷 손실 상황 재현
        err = a
        print("[pkt", a, "손실]")
        client_socket.sendall(str(err).encode()) # 수신자에 패킷 손실 상황 전달

    elif(a > 2): # 패킷 손실 이후 나머지 패킷 discarded 처리
        send1 = "pkt : " + str(a) + " - discarded"
        print("   send pkt :", a)
        client_socket.sendall(send1.encode())

time.sleep(3) # 패킷 손실로 인한 타이머
print("[Time-out... 재전송 시작]")
time.sleep(3)

data = client_socket.recv(1024) # 수신자로부터 time-out 정보 전달받음

if(data.decode() == 'reload'): 
    for a in range(base + 2, win_size): # time-out 이후 패킷 송신
        send2 = "pkt : " + str(a)
        print("   send pkt :", a)
        client_socket.sendall(send2.encode())
