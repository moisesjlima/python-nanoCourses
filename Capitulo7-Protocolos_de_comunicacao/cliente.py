from socket import *
server = "127.0.0.1"
port = 43210
'''
msg = bytes(input("Digite algo: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect(server, port)
obj_socket.send(msg)
response = obj_socket.recv(1024)
print("Recebemos: ", response)
obj_socket.close() '''

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((server, port))
    msg = bytes(input("Sua mensagem: "), 'utf-8')
    obj_socket.send(msg)
    response = obj_socket.recv(1024)
    print("Resposta do Servidor: ", str(response)[2:-1])
    if str(msg)[2:-1].upper() == "FIM":
        print("Conexão com servidor encerrada")
        break
obj_socket.close()