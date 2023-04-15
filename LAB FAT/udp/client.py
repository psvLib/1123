import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    c.sendto(("HELLO").encode("utf-8"),("localhost",12345))
    dat=c.recvfrom(1024)
    data=dat[0]
    print(data.decode("utf-8"))
    print(("FROM CLIENT: ").decode("utf-8"),data)
    