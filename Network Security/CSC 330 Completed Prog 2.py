def encrypt(plaintext, key, alphabet):
    ciphertext = ""
    # added the line below from google, it is what "wraps" the key if the shift is larger than the alphabet 
    key = int(key) % len(alphabet)
    for char in plaintext:
        if char in alphabet:
            i = alphabet.index(char)
            i = (i + key) % len(alphabet)
            ciphertext += alphabet[i]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key, alphabet):
    plaintext = ""
    # added the line below from google, it is what "wraps" the key if the shift is larger than the alphabet 
    key = int(key) % len(alphabet)
    for char in ciphertext:
        if char in alphabet:
            i = alphabet.index(char)
            i = (i - key) % len(alphabet)
            plaintext += alphabet[i]
        else:
            plaintext += char
    return plaintext


alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#^()_+=/"
key = input("Enter the key: ")


with open('chaloutput.txt', 'r') as file:
    ciphertext = file.read()

plaintext = decrypt(ciphertext, key, alphabet)
print(plaintext)

# this is from chat gpt, uses brute force to check 1-100 key if you dont know the key 
#for key in range(100):
 #   plaintext = decrypt(ciphertext, key, alphabet)
  #  print(f"Key {key}: {plaintext[:100]} \n")


with open("output2.txt", "w") as output_file:
    output_file.write(plaintext)
    print("Done")

