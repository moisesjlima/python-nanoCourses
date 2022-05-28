from socket import *
server = "127.0.0.1"
port = 43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, port))  
saida=""
while saida != "X":
  msg = input("Sua mensagem: ")
  obj_socket.sendto(msg.encode(), (server,port))
  dados, origem = obj_socket.recvfrom(65535)
  print("Resposta do Servidor:", dados.decode())
  saida= input("Digite <X> para sair: ").upper()
obj_socket.close()