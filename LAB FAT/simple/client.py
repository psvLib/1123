import socket
csock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

csock.connect(('127.0.0.1',12345))
msg="HELLO"
connMsg="CONNECTION ESTABLISHED"
csock.send(connMsg.encode("utf-8"))
while True:
    data=csock.recv(1024)
    if not data or data.decode("utf-8")=='END':
            break
    print("FROM SERVER: ",data.decode("utf-8"))

    msg=input("\nTO SEND TO SERVER[x]: ")
    if msg.lower()=='x':
        break
    csock.send(msg.encode("utf-8"))
csock.close()