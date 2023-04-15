import socket
server=socket.socket()
server.bind(("127.0.0.1",12345))
server.listen(1)

wsize=4
seqno=1
