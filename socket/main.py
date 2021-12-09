"""
 Implements a simple HTTP/1.0 Server

"""
import socket
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)
    
    # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Get the content of the file
    if filename == '/':
      filename = '/index.html'
    
    try:
      rel_path = "htdocs" + filename
      abs_file_path = os.path.join(script_dir, rel_path)
      fin = open(abs_file_path)
      content = fin.read()
      fin.close()
      response = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:
      response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
    
    # Get the content of htdocs/index.html
    # rel_path = "htdocs/index.html"
    # abs_file_path = os.path.join(script_dir, rel_path)
    # fin = open(abs_file_path)
    # content = fin.read()
    # fin.close()

    # Send HTTP response
    # response = 'HTTP/1.0 200 OK\n\nHello World'
    # client_connection.sendall(response.encode())
    # response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()