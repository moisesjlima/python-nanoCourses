from datetime import datetime
"""arquivo = open("teste2.txt", "w") # r - read/ a - append/ x - exclusive/ w - write

nome = input("Qual seu nome? ")
date = datetime()

arquivo.write("Bem vindo " + nome)
arquivo.close() 

date = datetime.today()
#print(date)
logs = input("Qual seu nome? ")
with open("teste3.txt", "a") as arquivo: #quando utilizado o with no final ele fecha o arquivo após executar o bloco de código
    arquivo.write("\nEscrito pelo " + logs + " com bloco with com o parametro append " ) 
"""

with open("teste3.txt", "r") as arquivo:
    #conteudo = arquivo.readlines()
    for linha in arquivo.readlines():
        print(linha)
