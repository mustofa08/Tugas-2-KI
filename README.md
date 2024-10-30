# Tugas-2

```
Nama  : Akhmad Mustofa Solikin
Nrp   : 5025211230
Kelas : Keamanan Informasi B
```

# Proyek Enkripsi dan Dekripsi dengan DES

Proyek ini adalah implementasi dari algoritma DES (Data Encryption Standard) untuk mengenkripsi dan mendekripsi pesan yang dikirim antara klien dan server menggunakan socket programming di Python. Proyek ini terdiri dari tiga file utama: `des.py`, `socket_server.py`, dan `socket_client.py`.

## Daftar Isi
- [des.py](#despy)
- [socket_server.py](#socket_serverpy)
- [socket_client.py](#socket_clientpy)
- [Cara Menjalankan](#cara-menjalankan)

---

## des.py

File ini berisi fungsi-fungsi untuk mengkonversi data antara format heksadesimal dan biner, serta fungsi untuk mengenkripsi dan mendekripsi pesan. Berikut adalah penjelasan setiap fungsi:

### Fungsi-fungsi:

1. **`hex_to_bin(s)`**:
   - Mengkonversi string heksadesimal menjadi string biner.
   - Input: string heksadesimal.
   - Output: string biner yang sesuai.

2. **`bin_to_hex(s)`**:
   - Mengkonversi string biner menjadi string heksadesimal.
   - Input: string biner.
   - Output: string heksadesimal yang sesuai.

3. **`string_to_hex(s)`**:
   - Mengkonversi string biasa menjadi representasi heksadesimal.
   - Input: string biasa.
   - Output: string heksadesimal yang sesuai.

4. **`hex_to_string(s)`**:
   - Mengkonversi string heksadesimal kembali menjadi string biasa.
   - Input: string heksadesimal.
   - Output: string biasa yang sesuai.

5. **`encrypt_block(pt, key)`**:
   - Placeholder untuk logika enkripsi blok menggunakan DES.
   - Input: plaintext (string) dan kunci (string).
   - Output: ciphertext dalam bentuk heksadesimal.

6. **`decrypt_block(ct, key)`**:
   - Placeholder untuk logika dekripsi blok menggunakan DES.
   - Input: ciphertext (string) dan kunci (string).
   - Output: plaintext (string).

7. **`encrypt_message(message, key)`**:
   - Mengenkripsi seluruh pesan dengan membagi menjadi blok.
   - Input: pesan (string) dan kunci (string).
   - Output: pesan terenkripsi dalam bentuk heksadesimal.

8. **`decrypt_message(message, key)`**:
   - Mendekripsi seluruh pesan dengan membagi menjadi blok.
   - Input: pesan terenkripsi (string) dan kunci (string).
   - Output: pesan asli (string).

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
