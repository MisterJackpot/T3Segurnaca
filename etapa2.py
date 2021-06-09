from Crypto.Cipher import AES
import sys

encrypted_message_hex = "FC6A9AA1BF05F7F7060599BA9992DF9D4B59D43B438CB5D5BF1DF881CFCF44A5FF0C48ABFB9926FC76406858E9190877C8AB65F208C6EE1CC40F5BFC636FBFB5EDA88C8E6DE23A6A94676D12864F77B9"
S = "a3c7d46aab83962cb7eebfa87b4d33bc"

bs = AES.block_size
message_bytes_array = bytes.fromhex(encrypted_message_hex)
IV = message_bytes_array[:16]
encrypted_message = message_bytes_array[16:]
senha = bytes.fromhex(S)

aes1 = AES.new(senha, AES.MODE_CBC, IV)
clear_text = aes1.decrypt(encrypted_message).decode()
print("Mensagem clara: " + str(clear_text))

reversed_clear_text = clear_text[::-1]
print(reversed_clear_text)
aes2 = AES.new(S, AES.MODE_CBC, IV)
cipher_text = aes2.encrypt(reversed_clear_text)

print(IV.hex() + cipher_text.hex())



# IV = 49563435495634354956343549563435
# message criptografada = 958d6f92b645c12b22172f22b1b38112
