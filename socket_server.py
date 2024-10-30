import socket
from des import encrypt_message, decrypt_message

KEY = "AABBCCDDEEFF1122"

def server_program():
    host = socket.gethostname()  # get the hostname
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(2)  # configure how many client the server can listen simultaneously
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    while True:
        encrypted_data = conn.recv(1024).decode()  # receive data stream
        if encrypted_data.lower() == 'bye':
            print("Mengakhiri koneksi")
            break

        print("Pesan terenkripsi diterima: " + encrypted_data)  # print received encrypted message
        decrypted_data = decrypt_message(encrypted_data, KEY)  # decrypt the message
        print("Pesan asli setelah dekripsi: " + decrypted_data)  # print original message

        response = input(" -> ")  # take input for response
        encrypted_response = encrypt_message(response, KEY)  # encrypt the response
        print("Pesan terenkripsi yang dikirim: " + encrypted_response)  # print encrypted response
        conn.send(encrypted_response.encode())  # send encrypted response to client

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()
