from Crypto.Cipher import AES
import sys
from base64 import b64encode
from os import urandom

encrypted_message_hex = "bf24ed9438a553f2bae45b13a869f6bb9ffa59436b580b0d2dbd09778da5d893aec0583b3beb0bcd0aab6dafae9664e90fb7cba5dfa24984eb018a135771e5ee1d87b64c742ab36cd06e50e8f49aa6a1"
S = "a3c7d46aab83962cb7eebfa87b4d33bc"

bs = AES.block_size
message_bytes_array = bytes.fromhex(encrypted_message_hex)
IV = message_bytes_array[:16]
encrypted_message = message_bytes_array[16:]
senha = bytes.fromhex(S)

aes1 = AES.new(senha, AES.MODE_CBC, IV)
clear_text = aes1.decrypt(encrypted_message).decode().strip()
print("Mensagem clara: " + str(clear_text))

reversed_clear_text = bytes(clear_text[::-1].encode('utf-8'))
print(reversed_clear_text)
IV = urandom(16)
length = 16 - (len(reversed_clear_text) % 16)
reversed_clear_text += bytes([length])*length

cipher = AES.new(senha, AES.MODE_CBC, IV)
cipher_text = cipher.encrypt(reversed_clear_text)
print(IV.hex() + cipher_text.hex())



# IV = 49563435495634354956343549563435
# message criptografada = 958d6f92b645c12b22172f22b1b38112
