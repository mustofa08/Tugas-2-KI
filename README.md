# Tugas-2

```
Nama  : Akhmad Mustofa Solikin
Nrp   : 5025211230
Kelas : Keamanan Informasi B
```

# Proyek Enkripsi dan Dekripsi dengan DES

Proyek ini adalah implementasi dari algoritma DES (Data Encryption Standard) untuk mengenkripsi dan mendekripsi pesan yang dikirim antara klien dan server menggunakan socket programming di Python. Proyek ini terdiri dari tiga file utama: `des.py`, `socket_server.py`, dan `socket_client.py`.


## des.py

File ini berisi fungsi-fungsi untuk mengkonversi data antara format heksadesimal dan biner, serta fungsi untuk mengenkripsi dan mendekripsi pesan. Berikut adalah penjelasan setiap fungsi:

1. Konversi Hexadecimal ke Biner

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

2. Konversi Biner ke Hexadecimal
   
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
     
3. Konversi String ke Hexadecimal

```
def string_to_hex(s):
    return ''.join(format(ord(i), 'x') for i in s)
```
   - Fungsi ini mengubah string biasa (plaintext) menjadi string heksadesimal.
   - Menggunakan ord(i) untuk mendapatkan nilai ASCII dari setiap karakter dan format(..., 'x') untuk mengkonversi nilai tersebut menjadi heksadesimal.
   - Output adalah string heksadesimal yang merupakan representasi dari karakter-karakter dalam string input.
     
4. Konversi Hexadecimal ke String

```
def hex_to_string(s):
    return ''.join(chr(int(s[i:i+2], 16)) for i in range(0, len(s), 2))
```
   - Fungsi ini mengkonversi string heksadesimal kembali menjadi string biasa.
   - Mengambil dua karakter heksadesimal, mengkonversinya menjadi bilangan bulat dengan basis 16, dan kemudian menggunakan chr(...) untuk mendapatkan karakter dari nilai tersebut.
   - Output adalah string asli yang dihasilkan dari konversi.
     
5. Enkripsi Blok
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
     
6. Dekripsi Blok

```
def decrypt_block(ct, key):
    # Placeholder for actual DES decryption logic
    # Convert ciphertext from hex back to string
    return hex_to_string(ct)  # Replace this with the actual decryption logic
```
   - Fungsi ini berfungsi untuk mendekripsi satu blok dari ciphertext.
   - Saat ini, fungsi ini hanya mengembalikan ciphertext yang telah dikonversi kembali menjadi string biasa sebagai placeholder untuk logika dekripsi DES yang sebenarnya.
     
7. Enkripsi Pesan
```
def encrypt_message(message, key):
    # Encrypt entire message by breaking it into blocks
    return "".join(encrypt_block(message[i:i+8], key) for i in range(0, len(message), 8))
```
   - Fungsi ini mengenkripsi seluruh pesan dengan memecahnya menjadi blok-blok yang lebih kecil (maksimal 8 karakter).
   - Menggunakan encrypt_block untuk mengenkripsi setiap blok dan menggabungkan hasilnya.
   - Output adalah string yang berisi pesan terenkripsi.
     
8. Dekripsi Pesan
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

File ini mengimplementasikan server yang menerima pesan dari klien, mendekripsi pesan, dan mengirimkan balasan yang terenkripsi kembali ke klien.

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
