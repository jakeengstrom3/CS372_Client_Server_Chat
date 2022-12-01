# User input from https://www.w3schools.com/python/python_user_input.asp
# Socket Programming reference https://www.geeksforgeeks.org/socket-programming-python/


import socket

addr = ('localhost', 7777) # Where the server is going to listen for connections
welcome_message = "Type /q to quit\nEnter message to send...\n"


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Options copied from Project Primer
s.bind(addr) # Bind socket to host:localhost port:7777
s.listen()

print("Server Listening on: " + str(addr[0]) + " at port: " + str(addr[1]))

client, addr = s.accept() # Accept client connection
print("Accepted connection from: " + str(addr)) 
client.send(welcome_message.encode()) # Send client welcome message

while True: # Loop forever (or until user quits)
    print("Waiting for client to send message...")
    response = client.recv(4500).decode() # Receive a message from the client

    if str(response) == "/q": # Check if the connection was closed by the client
        client.close()        
        s.close()
        break

    print(str(response)) # Print the message

    message = input(">")
    client.send(message.encode()) # Send new message
 
    if str(message) == "/q": # Check if server user closed the connection
        client.close()
        s.close()
        break

print("Connection closed")
