import socket

HOST = '127.0.0.1'
PORT = 80

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()

client_socket, addr = server_socket.accept()

print('connected by', addr)

while True:
    data = client_socket.recv(1024)
    print('received from', addr, data.decode())
    
    if (data.decode() == 'GET 200'):
        client_socket.sendall('''GET HTTP/1.1 200 OK\r\nContent-Encoding: gzip\r\nAccept-Ranges: bytes\r\nCache-Control: max-age=604800\r\nContent-Type: text/html; charset=UTF-8\r\nServer: kookmin/computernetwork\r\nHost: PYTHON internal server\r\n\r\n'''.encode())

    elif (data.decode() == 'GET 404'):
        client_socket.sendall('''GET HTTP/1.1 404 Not Found\r\nContent-Encoding: gzip\r\nAccept-Ranges: bytes\r\nCache-Control: max-age=604800\r\nContent-Type: text/html; charset=UTF-8\r\nServer: kookmin/computernetwork\r\nHost: PYTHON internal server\r\n\r\n'''.encode())

    elif (data.decode() == 'HEAD 100'):
        client_socket.sendall('''HEAD HTTP/1.1 100 Continue\r\nContent-Encoding: gzip\r\nAccept-Ranges: bytes\r\nCache-Control: max-age=604800\r\nContent-Type: text/html; charset=UTF-8\r\nServer: kookmin/computernetwork\r\nHost: PYTHON internal server\r\n\r\n'''.encode())

    elif (data.decode() == 'POST 200'):
        client_socket.sendall('''POST HTTP/1.1 200 OK\r\nContent-Encoding: gzip\r\nAccept-Ranges: bytes\r\nCache-Control: max-age=604800\r\nContent-Type: text/html; charset=UTF-8\r\nServer: kookmin/computernetwork\r\nHost: PYTHON internal server\r\n\r\n'''.encode())

    elif (data.decode() == 'POST 500'):
        client_socket.sendall('''POST HTTP/1.1 500 Internal Server Error\r\nContent-Encoding: gzip\r\nAccept-Ranges: bytes\r\nCache-Control: max-age=604800\r\nContent-Type: text/html; charset=UTF-8\r\nServer: kookmin/computernetwork\r\nHost: PYTHON internal server\r\n\r\n'''.encode())

    else:
        print("SOCKET closed... END")
        server_socket.close()
        break
