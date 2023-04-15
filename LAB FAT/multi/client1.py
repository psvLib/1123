import socket
c=socket.socket()
c.connect(("127.0.0.1",12345))

while True:
    data=c.recv(1024)
    print(data.decode("utf-8"))
    
    x=input("ENTER TO SEND MSG")
    c.send(("HELLO FROM C1").encode("utf-8"))

