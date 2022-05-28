import os
from ftplib import *

ftp_ativo = False
ftp = FTP(input("FTP que deseja se conectar: "))
print(ftp.getwelcome())

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)
print("Conexão bem sucedida no diretório: ", ftp.pwd())

menu = "1"
while menu == "1" or menu == "2" or menu == "3":
    menu = input(
        "Escolha a opção desejada: \n<1> - Para listar arquivos\n<2> - Para definir um diretório\n<3> - Para baixar um arquivo\n: ")
    if menu == "1":
        print(ftp.dir())
    elif menu == "2":
        ftp.cwd(input("Diretório que deseja entrar: "))
        print("Diretório corrente é: ", ftp.pwd())
    elif menu == "3":
        tipo = input(
            "<B> Para arquivo binário ou qualquer outro para arquivo ASCII: ").upper()
        if tipo == "B":
            with open(input("Nome do arquivo Binário destino: "), "wb") as arq:
                ftp.retrbinary('RETR ' + input("Arquivo origem: "), arq.write)
        else:
            with open(input("Nome do arquivo destino: "), "w") as arq:
                def escreverLinhas(data):
                    arq.write(data)
                    arq.write(os.linesep)
                ftp.retrlines(
                    'RETR ' + input("Arquivo de origem: "), escreverLinhas)
        print("Baixado com sucesso!")
ftp.quit()
