import socket

s=socket.socket()
print("socket sucessfully created")
port=40674

s.bind(('',port))
print("socket binded to %s" %(port))
s.listen(5)
print("socket is listening")

while True:

    c,addr=s.accept()
    print('Got connection from',addr)
    print(c)
    c.send(b'Thank you for connecting')
    print(c)
    c.close()