from Crypto.Cipher import AES
from os import urandom

# Variaveis Alteraveis: S = Hex da senha; encrypted_message_hex = Mensagem encriptada em hexadecimal
encrypted_message_hex = "bf24ed9438a553f2bae45b13a869f6bb9ffa59436b580b0d2dbd09778da5d893aec0583b3beb0bcd0aab6dafae9664e90fb7cba5dfa24984eb018a135771e5ee1d87b64c742ab36cd06e50e8f49aa6a1"
S = "a3c7d46aab83962cb7eebfa87b4d33bc"

# Adiciona padding a mensagem caso esta não esteja com tamanho de 16 bytes
def pad(text):
    length = 16 - (len(text) % 16)
    text += bytes([length]) * length
    return text

# Transforma a mensagem de hexadecimal para uma lista de bytes e separa a mensagem e o IV
message_bytes_array = bytes.fromhex(encrypted_message_hex)
IV = message_bytes_array[:16]
encrypted_message = message_bytes_array[16:]

# Pega os bytes da chave
S = bytes.fromhex(S)

# Decifra a mensagem utilizando a chave e o deslocamento IV
aes1 = AES.new(S, AES.MODE_CBC, IV)
clear_text = aes1.decrypt(encrypted_message).decode().strip()
print("Mensagem clara: " + str(clear_text))

# Inverte a mensagem recebida e adiciona o padding se necessario
reversed_clear_text = bytes(clear_text[::-1].encode('utf-8'))
reversed_clear_text = pad(reversed_clear_text)

# Gera um novo IV aleatorio para anexar no envio da mensagem
IV = urandom(16)

# Cifra a mensagem invertida, adcionando o IV ao inicio da mensagem
cipher = AES.new(S, AES.MODE_CBC, IV)
cipher_text = cipher.encrypt(reversed_clear_text)
print(IV.hex() + cipher_text.hex())

