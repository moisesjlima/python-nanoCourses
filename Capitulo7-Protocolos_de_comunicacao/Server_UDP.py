# TCP - Transfer Control Protocol | UDP - User Datagram Protocol
from socket import *

server = "127.0.0.1"
port = 43210
# AF_INET -> Identificação do emissor/receptor por IP ou DNS| SOCK_DGRAM -> Utilização do protocolo UDP
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((server, port))  # ligar conexão
print("Aguardando .....")
while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem............:", origem)
    # decode -> Exibe dados Bytes no formato string
    print("Origem............:", dados.decode())
    resposta = input("Digite sua resposta: ")
    # encode -> Converte string para Bytes
    obj_socket.sendto(resposta.encode(), origem)
obj_socket.close()
