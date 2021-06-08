import math
import random

# Valores hexadecimais fornecidos
hex_p = "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371"
hex_g = "A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5"

# Gerar valor a
decimal_a = random.getrandbits(1000)
print("a: " + str(decimal_a))
# Valor de a gerado para mensagem do professor: 1437164750761605896701117613557156711703278328311910170042266207183552797139995898043534547594174289402292831101412633084981942889105557808587999290485070339209987904875898562467552403708869055525271608388217500018083529186752709686449691968589037246150975888355122424681103568576623713654541411202331

# Transformando valores hexadecimais em decimais para calculo
decimal_p = int(hex_p, 16)
print("p: " + str(decimal_p))

decimal_g = int(hex_g, 16)
print("g: " + str(decimal_g))

# Calculo de valor A: (g^a) mod p
decimal_A = pow(decimal_g, decimal_a, decimal_p)
print("Valor decimal A: " + str(decimal_A))
hex_A = hex(decimal_A)

print("Valor hexadecimal A: " + str(hex_A))