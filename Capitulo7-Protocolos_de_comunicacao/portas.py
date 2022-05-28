import socket

print(socket.getservbyname("domain"))
print(socket.getservbyname("http"))
print(socket.getservbyname("https"))
print(socket.getservbyname("ftp"))
print(socket.getservbyname("smtp"))
