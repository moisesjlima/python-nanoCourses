import socket  # Biblioteca que estabelece comunicação entre dois processos
resp = "S"
while(resp == "S"):
    url = input("Digite uma URL: ")
    ip = socket.gethostbyname(url)
    print("O IP referente à URL informada '", url, "' é ", ip)
    resp = input("'S' para continuar: ").upper()

