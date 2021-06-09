from Crypto.Cipher import AES
from os import urandom
# Exemplo de execução e parametros do trabalho para processar a mensagem recebida e enviar esta invertida
# Executar o programa podendo alterar os valores de encrypted_message_hex e password
# Valor de password utilizado: a3c7d46aab83962cb7eebfa87b4d33bc
# Mensagem utilizada: FC6A9AA1BF05F7F7060599BA9992DF9D4B59D43B438CB5D5BF1DF881CFCF44A5FF0C48ABFB9926FC76406858E9190877C8AB65F208C6EE1CC40F5BFC636FBFB5EDA88C8E6DE23A6A94676D12864F77B9
# Mensagem obtida após execução: 823da9b606b9bf977426c509a317ab54ba95e63914b83f5ee8caffb0f7fd142e15a390fe87d5b4ca24f3d2d6fb132b9dd843bbe19a5ba12072804eae516aa1fd8c6c22266d6a6cf2b7b26171b2846534


# Variaveis Alteraveis: S = Hex da senha; encrypted_message_hex = Mensagem cifrada em hexadecimal
encrypted_message_hex = "0B3AC97F5D973A98EB13EEEF8A3B4433B660CD4E4316528AC3FDC04E21804F5D6DE36C3B698CBBBAAD49011882A73B468826DA5EE7C4F42C716D78130F719C814A1CA2B55D35D077649AB15DA96694ECC60571566F445C032DCB0013B00D195142CBBD018A32802A7110923AB5A9CD2D8FA85B4594C5104BE2D74680B857C08B80B51916E3D308EB07827C58B59282AA4282D2BC57EE949232B1196B67FD65D6"
password = "a3c7d46aab83962cb7eebfa87b4d33bc"

# Adiciona padding a mensagem para ficar multiplo de 16 bytes
def pad(text):
    length = 16 - (len(text) % 16)
    text += bytes([length]) * length
    return text


# Transforma a mensagem de hexadecimal para uma lista de bytes e separa a mensagem e o IV
message_bytes = bytes.fromhex(encrypted_message_hex)
IV = message_bytes[:16]
encrypted_message = message_bytes[16:]

# Converte a chave para bytes
password = bytes.fromhex(password)

# Decifra a mensagem utilizando a chave e o deslocamento IV
aes = AES.new(password, AES.MODE_CBC, IV)
clear_text = aes.decrypt(encrypted_message).decode('utf-8').strip()
print("Mensagem clara: " + str(clear_text))

# Inverte a mensagem recebida e adiciona o padding se necessario
reversed_clear_text = bytes(clear_text[::-1].encode('utf-8'))
reversed_clear_text = pad(reversed_clear_text)

# Gera um novo IV aleatorio para anexar no envio da mensagem
IV = urandom(16)

# Cifra a mensagem invertida, adcionando o IV ao inicio da mensagem
cipher = AES.new(password, AES.MODE_CBC, IV)
cipher_bytes = cipher.encrypt(reversed_clear_text)
print("Mensagem invertida: " + (IV.hex() + cipher_bytes.hex()))
