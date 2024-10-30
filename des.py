# des.py

def hex_to_bin(s):
    mp = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100",
          '5': "0101", '6': "0110", '7': "0111", '8': "1000", '9': "1001",
          'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
    return "".join(mp[i] for i in s)

def bin_to_hex(s):
    mp = {"0000": '0', "0001": '1', "0010": '2', "0011": '3',
          "0100": '4', "0101": '5', "0110": '6', "0111": '7',
          "1000": '8', "1001": '9', "1010": 'A', "1011": 'B',
          "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}
    return "".join(mp[s[i:i+4]] for i in range(0, len(s), 4))

def encrypt_block(pt, key):
    # Placeholder untuk enkripsi satu blok 64-bit
    return pt  # Implementasi DES seharusnya ada di sini

def decrypt_block(ct, key):
    # Placeholder untuk dekripsi satu blok 64-bit
    return ct  # Implementasi DES seharusnya ada di sini

def encrypt_message(message, key):
    # Enkripsi seluruh pesan dengan memecahnya menjadi blok-blok
    return "".join(encrypt_block(message[i:i+16], key) for i in range(0, len(message), 16))

def decrypt_message(message, key):
    # Dekripsi seluruh pesan dengan memecahnya menjadi blok-blok
    return "".join(decrypt_block(message[i:i+16], key) for i in range(0, len(message), 16))
