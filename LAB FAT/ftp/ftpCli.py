import socket
import tqdm

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000
BUFFER_SIZE = 1024
SEPARATOR = '<SEPARATOR>'

# create the client socket
s = socket.socket()

# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

# receive the list of files from the server
message = s.recv(BUFFER_SIZE).decode()
print(f"List of files: {message}")

# send the filename to the server and receive the file
filename = input("Enter the filename: ")
s.send(filename.encode())
response = s.recv(BUFFER_SIZE).decode()
if response == "File not found":
    print(response)
else:
    filename, filesize = response.split(SEPARATOR)
    filesize = int(filesize)
    with open(filename, 'wb') as f:
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
            progress.update(len(data))
    print(f"{filename} received.")

# close the connection
s.close()
