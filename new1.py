import socket
hostname=socket.gethostname()
print(hostname)

ipadd=socket.gethostbyname(hostname)
print(ipadd)


