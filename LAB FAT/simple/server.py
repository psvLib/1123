import socket
ssock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ssock.bind(('127.0.0.1',12345))
print("BOUND")
ssock.listen(5)
while True:
    csock,addr=ssock.accept()
    print("CONNECTED TO ",addr)
    connMsg="CONNECTION ESTABLISHED"
    csock.send(connMsg.encode("utf-8"))
    while True:
        data=csock.recv(1024)
        if not data or data.decode("utf-8")=='END':
            break
        print("FROM CLIENT: ",data.decode("utf-8"))
        msg=input("\nTO SEND TO CLIENT[X to exit]: ")
        if msg.lower()=='x':
            break
        csock.send(msg.encode("utf-8"))
    csock.close()
ssock.close()