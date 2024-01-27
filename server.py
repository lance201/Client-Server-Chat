import socket

# Code reference from Computer Networking: A Top Down Approach, pg 193-194

serverPort = 8001
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
localhost = socket.gethostbyname(hostname)

# Binds socket to designated port
serverSocket.bind((localhost, serverPort))
serverSocket.listen(1)
print(f"The server is listening on localhost on port: {serverPort}")

connectionSocket, addr = serverSocket.accept()

# Print connected message
print(f"Connected by {addr}")
print("Waiting for message...")

# Loop to keep server running continuously
while True:

    # Receive and print requests
    req = connectionSocket.recv(4096).decode()

    # Check is received data is "/q"
    if req == "/q":
        connectionSocket.close()
        break
    else:
        print(req)

    # Send and print server data
    data = input("Enter message to send...\n>")
    connectionSocket.send(data.encode())