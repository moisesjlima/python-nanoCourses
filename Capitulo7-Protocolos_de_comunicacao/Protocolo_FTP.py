from ftplib import *
ftp_ativo = False
#ftp = FTP('ftp.ibiblio.org')
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input("Digite o usuário: ")
senha = input("Digite a Senha: ")
ftp.login(usuario, senha)#Se for necessario caso não seja público

print("Diretório atual de trabalhos", ftp.pwd())
ftp.cwd('pub')
print("Diretório corrente: ", ftp.pwd())
print(ftp.retrlines('LIST'))
ftp.quit()
