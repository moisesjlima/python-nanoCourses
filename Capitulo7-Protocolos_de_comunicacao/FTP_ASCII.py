import os
from ftplib import *


def escreverLinhas(data):
    arq.write(data)
    arq.write(os.linesep)


ftp_ativo = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
arquivo = 'LEAIME'
ftp.set_pasv(ftp_ativo)
with open(arquivo, 'w') as arq:
    ftp.retrlines('RET README', escreverLinhas)
ftp.quit()
