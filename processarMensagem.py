from Crypto.Cipher import AES
from os import urandom

# Variaveis Alteraveis: S = Hex da senha; encrypted_message_hex = Mensagem cifrada em hexadecimal
encrypted_message_hex = "FC6A9AA1BF05F7F7060599BA9992DF9D4B59D43B438CB5D5BF1DF881CFCF44A5FF0C48ABFB9926FC76406858E9190877C8AB65F208C6EE1CC40F5BFC636FBFB5EDA88C8E6DE23A6A94676D12864F77B9"
S = "a3c7d46aab83962cb7eebfa87b4d33bc"

# Adiciona padding a mensagem caso esta não esteja com tamanho de 16 bytes
def pad(text):
    length = 16 - (len(text) % 16)
    text += bytes([length]) * length
    return text

# Transforma a mensagem de hexadecimal para uma lista de bytes e separa a mensagem e o IV
message_bytes = bytes.fromhex(encrypted_message_hex)
IV = message_bytes[:16]
encrypted_message = message_bytes[16:]

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
