import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("127.0.0.1",12345))

while True:
    try:
        msg=c.recv(1024)
    except:
        continue
    if msg:
        print("SERVER: ",msg.decode("utf-8"))
        c.send(input("YOU:").encode("utf-8"))
    else:
        c.send(input("YOU:").encode("utf-8"))

