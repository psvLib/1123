import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",12345))
s.listen(5)

while True:
    c,addr=s.accept()
    data=c.recv(1024)
    arr={}
    

