import socket

'''
=== 수신자 ===
TCP 기반 GO-BACK-N 프로토콜 구현
20175288 최광삼
'''

HOST = '127.0.0.1' # IP, 포트 경로 지정
PORT = 80

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP 소켓 설정

server_socket.bind((HOST, PORT)) # 소켓 경로 설정
server_socket.listen()

client_socket, addr = server_socket.accept()

print("[GO-BACK-N Protocol]")
print("----- Receiver -----")

base = 0 # BASE 초기화
win_size = 5 # 보낼 패킷량
count = 0 # 순번 초기화

for a in range(base, win_size):
    data = client_socket.recv(1024) # 소켓으로 패킷이 들어올때까지 대기
    
    if(data.decode()[-1] != '2'):
        print("   rcv " + data.decode())
        count = count + 1 # 순번 증가
    
    elif (data.decode() == '2'): # 패킷 손실로 인한 discarded
        print("[무응답 패킷] pkt : " + data.decode() + " - discarded")

        if(count == 2):
            client_socket.sendall("reload".encode()) # 송신자에 time-out 알림

            for i in range(win_size):
                newdata = client_socket.recv(1024) # time-out 후 패킷 수신
                print("   rcv " + newdata.decode())
