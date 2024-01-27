import socket

# Code reference from Computer Networking: A Top Down Approach, pg 193-194

Port = 8001
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
localhost = socket.gethostbyname(hostname)

# Connect to server
clientSocket.connect((localhost, Port))
print(f"The client is connected to localhost on port: {Port}")
print("Type /q to quit")

# Loop to keep client running continuously
while True:

    # Send and print client data
    data = input("Enter message to send...\n>")
    if data == "/q":
        clientSocket.send(data.encode())
        clientSocket.close()
        break
    else:
        clientSocket.send(data.encode())
        # Receive and print requests
        req = clientSocket.recv(4096).decode()
        print(req)
