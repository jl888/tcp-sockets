import socket

# Initializations
TCP_IP = '127.0.0.1'
TCP_PORT = 2000
BUFFER_SIZE = 1024

# 1. Create socket: Use IPv4 and Stream Socket (a TCP protocol for data transmission)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. Bind socket to a particular port number and IP address
server_socket.bind((TCP_IP, TCP_PORT))
# 3. Declare willingness to accept incoming connections. Queue up as many as 5 connect requests
server_socket.listen(5)
# 4. Accept an incoming connection request. Create a new socket for this connection
conn, addr = server_socket.accept()
print("Connection address: {}".format(addr[0]))

while 1:
    # 5. Recieve data from socket
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    # Decode message from UTF-8 to Unicode (string)
    data_str = data.decode()
    print("Received data: {}".format(data_str))
    # 6. Send data to socket
    conn.send(data)

# 7. Close connection
conn.close()
print("Connection closed")