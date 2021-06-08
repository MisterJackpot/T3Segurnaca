from Crypto.Cipher import AES
import sys


if __name__ == '__main__':
    encrypted_message_hex = sys.argv[1]
    S = sys.argv[2]

    message_bytes_array = bytes.fromhex(encrypted_message_hex)
    IV = message_bytes_array[:32]
    encrypted_message = message_bytes_array[32:]

    aes1 = AES.new(S, AES.MODE_CBC, IV)
    clear_text = aes1.decrypt(encrypted_message).decode('utf-8')
    print(clear_text)

    reversed_clear_text = clear_text[::-1]

    aes2 = AES.new(S, AES.MODE_CBC, IV)
    cipher_text = aes2.encrypt(reversed_clear_text)

    print(IV.hex() + cipher_text.hex())



# IV = 49563435495634354956343549563435
# message criptografada = 958d6f92b645c12b22172f22b1b38112
