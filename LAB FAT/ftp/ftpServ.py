import socket
import os

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
BUFFER_SIZE = 1024
SEPARATOR = '<SEPARATOR>'

# create the server socket
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# accept client connections
client_socket, address = s.accept()
print(f"[+] {address} is connected.")

# send the list of files to the client
files = os.listdir('.')
files.remove(__file__)
files.remove('.DS_Store')
message = ""
for file in files:
    message += file + SEPARATOR
client_socket.send(message.encode())

# receive the filename from the client and send the file
filename = client_socket.recv(BUFFER_SIZE).decode()
if os.path.isfile(filename):
    filesize = os.path.getsize(filename)
    client_socket.send(f"{filename}{SEPARATOR}{filesize}".encode())
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            client_socket.sendall(data)
else:
    client_socket.send("File not found".encode())

# close the connection
client_socket.close()
s.close()
