import socket

HOST = '127.0.0.1'
PORT = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    i = input("1에서 5까지 숫자를 입력하세요\n(종료하려면 Q) : ")

    if (i == 'q' or i == 'Q'):
        print("SOCKET closed... END")
        client_socket.sendall(i.encode())
        client_socket.close()
        break

    elif (i == 'GET 200' or i == 'GET 404' or i == 'HEAD 100' or i == 'POST 200' or i == 'POST 500'):
        client_socket.sendall(i.encode())
        data = client_socket.recv(1024)
        print(repr(data.decode()))

    else:
        print("올바른 숫자를 입력해주세요.")
