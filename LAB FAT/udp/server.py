import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("localhost",12345))
s.listen(5)
while True:
    dat=s.recvfrom(1024)
    data=dat[0]
    addr=dat[1]
    print(data.decode("utf-8"))
    print(("FROM CLIENT: ").decode("utf-8"),data)
    s.sendto(("HELLO").encode("utf-8"),addr)