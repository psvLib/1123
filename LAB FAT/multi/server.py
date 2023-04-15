import socket
from _thread import *
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

host="127.0.0.1"
addr=12345
ThreadCount=0
s.bind((host,addr))
s.listen(5)
#clients=[]
def newConnection(c,n):
    c.send(("WELCOME TO SERVER").encode("utf-8"))
    while True:
        reply=f"FROM SERVER: MESSAGE RECIEVED from {n}"
        data=c.recv(2048)
        print("RECVD MSG: ",data)
        print("REPLYING TO ALL...")
        if not data: 
            break
        c.send(reply.encode("utf-8"))
    c.close()
while True:
    c,addr=s.accept()
    #clients.append()
    
    print("Connected to ",addr, "Current no.of Threads",ThreadCount)
    start_new_thread(newConnection,(c,ThreadCount))
    ThreadCount+=1
