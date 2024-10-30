# Tugas-2

```
Nama  : Akhmad Mustofa Solikin
Nrp   : 5025211230
Kelas : Keamanan Informasi B
```

#Enkripsi dan Dekripsi dengan DES

Project ini adalah implementasi dari algoritma DES (Data Encryption Standard) untuk mengenkripsi dan mendekripsi pesan yang dikirim antara klien dan server menggunakan socket programming di Python. Proyek ini terdiri dari tiga file utama: `des.py`, `socket_server.py`, dan `socket_client.py`.


## des.py

File des.py adalah modul penting dalam proyek ini yang menangani semua fungsi terkait konversi data dan enkripsi/dekripsi menggunakan algoritma DES. Namun, fungsi enkripsi dan dekripsi aktual belum diimplementasikan dan harus diganti dengan logika DES yang sesuai agar fungsionalitasnya lengkap.

### 1. Konversi Hexadecimal ke Biner

   ```
   def hex_to_bin(s):
    mp = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100",
          '5': "0101", '6': "0110", '7': "0111", '8': "1000", '9': "1001",
          'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
    return "".join(mp[i] for i in s)
   ```

   - Fungsi ini mengubah string heksadesimal menjadi string biner.
   - Menggunakan kamus (mp) untuk memetakan setiap digit heksadesimal ke representasi biner 4-bitnya.
   - Output adalah string biner yang dihasilkan dengan menggabungkan semua representasi biner untuk setiap karakter dalam string input.

### 2. Konversi Biner ke Hexadecimal
   
```
def bin_to_hex(s):
    mp = {"0000": '0', "0001": '1', "0010": '2', "0011": '3',
          "0100": '4', "0101": '5', "0110": '6', "0111": '7',
          "1000": '8', "1001": '9', "1010": 'A', "1011": 'B',
          "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}
    return "".join(mp[s[i:i+4]] for i in range(0, len(s), 4))
```
   - Fungsi ini mengkonversi string biner menjadi string heksadesimal.
   - Menggunakan kamus (mp) untuk memetakan setiap 4-bit biner ke digit heksadesimal.
   - Output adalah string heksadesimal yang dihasilkan dengan menggabungkan representasi heksadesimal dari setiap blok 4-bit dalam string input.
     
### 3. Konversi String ke Hexadecimal

```
def string_to_hex(s):
    return ''.join(format(ord(i), 'x') for i in s)
```
   - Fungsi ini mengubah string biasa (plaintext) menjadi string heksadesimal.
   - Menggunakan ord(i) untuk mendapatkan nilai ASCII dari setiap karakter dan format(..., 'x') untuk mengkonversi nilai tersebut menjadi heksadesimal.
   - Output adalah string heksadesimal yang merupakan representasi dari karakter-karakter dalam string input.
     
### 4. Konversi Hexadecimal ke String

```
def hex_to_string(s):
    return ''.join(chr(int(s[i:i+2], 16)) for i in range(0, len(s), 2))
```
   - Fungsi ini mengkonversi string heksadesimal kembali menjadi string biasa.
   - Mengambil dua karakter heksadesimal, mengkonversinya menjadi bilangan bulat dengan basis 16, dan kemudian menggunakan chr(...) untuk mendapatkan karakter dari nilai tersebut.
   - Output adalah string asli yang dihasilkan dari konversi.
     
### 5. Enkripsi Blok
```
def encrypt_block(pt, key):
    # Convert plaintext to hex
    pt_hex = string_to_hex(pt)
    # Placeholder for actual DES encryption logic
    return pt_hex  # Replace this with the actual encryption logic
```
   - Fungsi ini berfungsi untuk mengenkripsi satu blok dari plaintext.
   - Pertama, plaintext dikonversi menjadi heksadesimal menggunakan fungsi string_to_hex.
   - Catatan: Saat ini, fungsi ini hanya mengembalikan plaintext yang telah dikonversi ke heksadesimal sebagai placeholder untuk logika enkripsi DES yang sebenarnya.
     
### 6. Dekripsi Blok

```
def decrypt_block(ct, key):
    # Placeholder for actual DES decryption logic
    # Convert ciphertext from hex back to string
    return hex_to_string(ct)  # Replace this with the actual decryption logic
```
   - Fungsi ini berfungsi untuk mendekripsi satu blok dari ciphertext.
   - Saat ini, fungsi ini hanya mengembalikan ciphertext yang telah dikonversi kembali menjadi string biasa sebagai placeholder untuk logika dekripsi DES yang sebenarnya.
     
### 7. Enkripsi Pesan
```
def encrypt_message(message, key):
    # Encrypt entire message by breaking it into blocks
    return "".join(encrypt_block(message[i:i+8], key) for i in range(0, len(message), 8))
```
   - Fungsi ini mengenkripsi seluruh pesan dengan memecahnya menjadi blok-blok yang lebih kecil (maksimal 8 karakter).
   - Menggunakan encrypt_block untuk mengenkripsi setiap blok dan menggabungkan hasilnya.
   - Output adalah string yang berisi pesan terenkripsi.
     
### 8. Dekripsi Pesan
```
def decrypt_message(message, key):
    # Decrypt entire message by breaking it into blocks
    return "".join(decrypt_block(message[i:i+16], key) for i in range(0, len(message), 16))
```
   - Fungsi ini mendekripsi seluruh pesan dengan memecahnya menjadi blok-blok yang lebih kecil (maksimal 16 karakter).
   - Menggunakan decrypt_block untuk mendekripsi setiap blok dan menggabungkan hasilnya.
   - Output adalah string yang berisi pesan yang telah didekripsi.

---

## socket_server.py

File socket_server.py bertanggung jawab untuk mengatur server yang dapat menerima koneksi dari klien, memproses pesan terenkripsi, mendekripsi pesan tersebut, dan mengirim kembali balasan terenkripsi. Server ini akan terus beroperasi hingga koneksi ditutup oleh klien atau terjadi kesalahan koneksi.

### 1. Import Libraries
```
import socket
from des import encrypt_message, decrypt_message
```
   - import socket: Mengimpor modul socket untuk menangani komunikasi jaringan.
   - from des import encrypt_message, decrypt_message: Mengimpor fungsi encrypt_message dan decrypt_message dari modul des.py untuk melakukan enkripsi dan dekripsi pesan.
     
### 2. Mendefinisikan Kunci Enkripsi
```
KEY = "AABBCCDDEEFF1122"
```
   - KEY: Mendefinisikan kunci yang digunakan untuk enkripsi dan dekripsi. Dalam hal ini, kunci adalah string heksadesimal yang berfungsi sebagai input untuk algoritma DES.
     
### 3. Fungsi server_program()
```
def server_program():
```
   - Mendefinisikan fungsi utama yang akan dijalankan oleh server.
     
### 4. Inisialisasi Socket Server
```
    host = socket.gethostname()  # get the hostname
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(2)  # configure how many client the server can listen simultaneously
```
   - host: Mengambil nama host mesin saat ini menggunakan socket.gethostname().
   - port: Mendefinisikan nomor port yang akan digunakan untuk komunikasi, dalam hal ini, port 5000.
   - server_socket: Membuat instance dari socket server.
   - bind((host, port)): Mengaitkan alamat host dan port ke socket agar dapat menerima koneksi.
   - listen(2): Mengatur jumlah maksimum koneksi klien yang dapat diterima secara bersamaan (dalam hal ini, hingga 2 klien).
   
### 5. Menerima Koneksi dari Klien
```
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
```
   - conn, address = server_socket.accept(): Menerima koneksi baru dari klien. conn adalah objek socket yang terhubung dengan klien, dan address adalah alamat IP serta port klien.
   - print("Connection from: " + str(address)): Menampilkan informasi alamat klien yang terhubung.
   
### 6. Loop untuk Menerima dan Mengirim Pesan
```
    while True:
        try:
            encrypted_data = conn.recv(1024).decode()  # receive data stream
```
   - Memulai loop tanpa henti untuk menerima dan mengirim pesan hingga koneksi ditutup.
   - conn.recv(1024).decode(): Menerima aliran data dari klien hingga 1024 byte dan mengubahnya menjadi string menggunakan metode decode().

### 7. Memeriksa Koneksi dan Mengolah Data
```
            if not encrypted_data:  # check if data is None or empty
                print("Koneksi terputus.")
                break
            
            if encrypted_data.lower() == 'bye':
                print("Mengakhiri koneksi")
                break
```
Pemeriksaan Koneksi:
   - Jika encrypted_data kosong, cetak pesan "Koneksi terputus" dan keluar dari loop.
   - Jika klien mengirim pesan "bye", cetak "Mengakhiri koneksi" dan keluar dari loop.
     
8. Dekripsi dan Mengirim Balasan
```
            print("Pesan terenkripsi diterima: " + encrypted_data)  # print received encrypted message
            decrypted_data = decrypt_message(encrypted_data, KEY)  # decrypt the message
            print("Pesan asli setelah dekripsi: " + decrypted_data)  # print original message

            response = input(" -> ")  # take input for response
            encrypted_response = encrypt_message(response, KEY)  # encrypt the response
            print("Pesan terenkripsi yang dikirim: " + encrypted_response)  # print encrypted response
            conn.send(encrypted_response.encode())  # send encrypted response to client
```
   - Setelah menerima data terenkripsi, tampilkan pesan tersebut.
   - Dekripsi data menggunakan decrypt_message dan tampilkan pesan asli.
   - Minta input dari pengguna untuk balasan yang akan dikirim ke klien.
   - Enkripsi balasan menggunakan encrypt_message dan tampilkan pesan terenkripsi yang akan dikirim.
   - Kirim pesan terenkripsi ke klien menggunakan conn.send().
   
### 9. Menangani Kesalahan Koneksi
```
        except (ConnectionResetError, ConnectionAbortedError):
            print("Koneksi terputus dengan klien.")
            break
```
   - Menangkap dan menangani kesalahan yang terjadi jika koneksi terputus secara mendadak. Jika terjadi kesalahan, tampilkan pesan bahwa koneksi terputus.
     
### 10. Menutup Koneksi
```
    conn.close()  # close the connection
    server_socket.close()  # close the server socket
```
   - Setelah keluar dari loop, tutup koneksi dengan klien dan tutup socket server.
     
### 11. Menjalankan Fungsi Server
```
if __name__ == '__main__':
    server_program()
```
   - Memeriksa apakah script dijalankan sebagai program utama, jika ya, maka panggil server_program() untuk memulai server.


### Cara Kerja:
1. Server mendengarkan koneksi dari klien di port yang ditentukan.
2. Setelah koneksi diterima, server menunggu untuk menerima pesan terenkripsi dari klien.
3. Server mendekripsi pesan yang diterima dan menampilkan pesan asli.
4. Server kemudian meminta input dari pengguna untuk merespons dan mengenkripsi pesan tersebut sebelum mengirimkan kembali ke klien.
5. Proses ini berulang sampai pengguna mengirimkan "bye", yang akan menghentikan koneksi.

---

## socket_client.py

File ini mengimplementasikan klien yang terhubung ke server, mengirim pesan terenkripsi, dan menerima balasan dari server.

### Cara Kerja:
1. Klien menghubungkan diri ke server di alamat dan port yang ditentukan.
2. Klien meminta input dari pengguna untuk mengirimkan pesan.
3. Pesan yang dimasukkan kemudian dienkripsi dan dikirim ke server.
4. Klien menerima balasan dari server, mendekripsi pesan, dan menampilkannya di terminal.
5. Proses ini berulang sampai pengguna mengirimkan "bye", yang akan menutup koneksi.

---

## Cara Menjalankan

1. Pastikan Anda memiliki Python terinstal di komputer Anda.
2. Jalankan `socket_server.py` di terminal pertama:
   ```bash
   python socket_server.py
