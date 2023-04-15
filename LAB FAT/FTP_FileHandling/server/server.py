import socket
ssock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ssock.bind(('127.0.0.1',12345))
print("BOUND")
ssock.listen(5)
csock,addr=ssock.accept()
filename=csock.recv(1024) 
filename=filename.decode("utf-8")  
print("filename recieved") 
fObj=open(filename,"r")
x=fObj.read()   
csock.send(x.encode("utf-8"))
        