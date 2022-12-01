# User input from https://www.w3schools.com/python/python_user_input.asp
# Socket Programming reference https://www.geeksforgeeks.org/socket-programming-python/


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Options copied from my project_1 code

s.connect(('localhost', 7777)) # Connect to the server
print("Connected to localhost at 7777")

while True:
    print("Waiting for server to send message...")
    response = s.recv(4500).decode() # Receive message from server

    if str(response) == "/q": # Check if server user closed the connection
        s.close()
        break

    print(str(response)) # Print the received message

    message = str(input(">")) 
    s.send(message.encode()) # Send new message

    if message == "/q": # Check if client user closed the connection
        s.close()
        break

print("Connection closed")
    