with open("start.txt", "rb") as f:
    ciphertext = f.read()

with open("key.txt", "rb") as f:
    key = f.read()

plaintext = bytearray(len(ciphertext))

# Added this key length from chatgpt -- works to xor even if the key and cipher text are not the same size
key_length = len(key)

for i in range(len(ciphertext)):
    plaintext[i] = ciphertext[i] ^ key[i % key_length]

with open("cha2.bin", "wb") as f:
    f.write(plaintext)
