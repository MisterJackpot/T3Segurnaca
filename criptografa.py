from Crypto.Cipher import AES

obj = AES.new('c2b1b713777115fc', AES.MODE_CBC, 'IV45IV45IV45IV45')
message = "a1a2a3a4a5a6a7a81"
ciphertext = obj.encrypt(message)

print('IV45IV45IV45IV45'.encode('utf-8').hex())
print(ciphertext.hex())

