import socket
from des import encrypt_message

KEY = "AABBCCDDEEFF1122"

def client_program():
    host = socket.gethostname()  # or use '127.0.0.1' if you run server on the same machine
    port = 5000  # the port on which the server is listening

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        encrypted_message = encrypt_message(message, KEY)  # encrypt the message before sending
        print("Pesan terenkripsi yang dikirim: " + encrypted_message)  # print the encrypted message
        client_socket.send(encrypted_message.encode())  # send the encrypted message

        # receive response from the server
        data = client_socket.recv(1024).decode()  
        print('Pesan dari server (terenkripsi): ' + data)  # show encrypted response from server

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
