import socket
from des import encrypt_message, decrypt_message

KEY = "AABBCCDDEEFF1122"

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        encrypted_message = encrypt_message(message, KEY)  # encrypt the message
        client_socket.send(encrypted_message.encode())  # send message
        print('Pesan terenkripsi yang dikirim: ' + encrypted_message)  # show sent message

        data = client_socket.recv(1024).decode()  # receive response
        decrypted_data = decrypt_message(data, KEY)  # decrypt the response
        print('Received from server: ' + decrypted_data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
