import socket
csock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

csock.connect(('127.0.0.1',12345))
filename="f1.txt"
csock.send(filename.encode("utf-8"))
data=(csock.recv(2048)).decode("utf-8")
print("filedata recieved")
fobj=open(filename,"w+")
fobj.write(data)
filedata=fobj.read()
print(filedata)
arr=filedata.split(" ")
print(arr)

