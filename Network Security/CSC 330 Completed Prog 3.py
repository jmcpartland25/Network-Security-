alphabet = "/=+_)(^#@ZYXWVUTSRQPONMLKJIHGFEDCBA9876543210zyxwvutsrqponmlkjihgfedcba"

key = "Bandit"

def encrypt(plaintext, key):
#used chat cpt to work this back and forth which eventually led me to add the key_expanded
    # the key_expanded works to take each letter in the key and find it postion in the aplhabet and key_len then helps with the shift
    ciphertext = ""
    k = 0
    key_expanded = [alphabet.index(kc) for kc in key if kc in alphabet]
    key_len = len(key_expanded)
    
    for char in plaintext:
        if char in alphabet:
            i = alphabet.index(char)
            k_i = key_expanded[k % key_len]
            i = (i + k_i) % len(alphabet)
            ciphertext += alphabet[i]
            k += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    #used chat cpt to work this back and forth which eventually led me to add the key_expanded
    # the key_expanded works to take each letter in the key and find it postion in the aplhabet and key_len then helps with the shift
    plaintext = ""
    k = 0
    key_expanded = [alphabet.index(kc) for kc in key if kc in alphabet]
    key_len = len(key_expanded)
    
    for char in ciphertext:
        if char in alphabet:
            i = alphabet.index(char)
            k_i = key_expanded[k % key_len]
            i = (i - k_i) % len(alphabet)
            plaintext += alphabet[i]
            k += 1
        else:
            plaintext += char
    return plaintext

input_filename = 'output2.txt'

with open(input_filename, 'r') as file:
    ciphertext = file.read()
    
#This works to print otgether if text is one single long line
decrypted_text = decrypt(ciphertext, key)
#this helps to print if the text is lines
#decrypted_text = "".join([decrypt(line, key) for line in ciphertext])


print(decrypted_text)