import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1",12345))
s.listen(1)

c,addr=s.accept()
c.send(("CONNECTED TO SERVER").encode("utf-8"))
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

