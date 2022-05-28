from socket import *
server = "127.0.0.1"
port = 43210
# AF_INET -> Identificação do emissor/receptor por IP ou DNS| SOCK STREAM -> Utilização do protocolo TCP
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server, port))
obj_socket.listen(2)
print("Aguardando cliente.....")
while True:
    con, client = obj_socket.accept()
    print("Conectado com ", client)
    while True:
        msg_received = str(con.recv(1024))
        print("Recebemos: ", str(msg_received)[2:-1])
        msg_sent = bytes(input("sua Resposta: "), "utf-8")
        con.send(msg_sent)
    con.close()
