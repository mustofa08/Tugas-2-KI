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

def string_to_hex(s):
    return ''.join(format(ord(i), 'x') for i in s)

def hex_to_string(s):
    return ''.join(chr(int(s[i:i+2], 16)) for i in range(0, len(s), 2))

def encrypt_block(pt, key):
    # Convert plaintext to hex
    pt_hex = string_to_hex(pt)
    # Placeholder for actual DES encryption logic
    return pt_hex  # Replace this with the actual encryption logic

def decrypt_block(ct, key):
    # Placeholder for actual DES decryption logic
    # Convert ciphertext from hex back to string
    return hex_to_string(ct)  # Replace this with the actual decryption logic

def encrypt_message(message, key):
    # Encrypt entire message by breaking it into blocks
    return "".join(encrypt_block(message[i:i+8], key) for i in range(0, len(message), 8))

def decrypt_message(message, key):
    # Decrypt entire message by breaking it into blocks
    return "".join(decrypt_block(message[i:i+16], key) for i in range(0, len(message), 16))
