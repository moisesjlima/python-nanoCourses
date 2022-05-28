from ftplib import *
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
ftp.cwd('Directory')
with open('Pai do lunix.jpg', 'wb') as arq:
    ftp.retrbinary('RETR linus-father-of-linux', arq.write)
ftp.quit()
