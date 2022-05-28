resposta = "SIM"

while resposta == "SIM":
    resposta = input("Deseja continuar: [SIM/NAO]").upper()
    if resposta == "SIM":
        print("Continuar")

print("Finalizou")