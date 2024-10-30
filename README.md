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
