with open("encoded.txt", "r") as file:
    lines = file.readlines()

#this automaticially checks and choose if the binary is written in 7 or 8 bits 
if lines and len(lines[0].strip()) % 8 == 0:
    BITS = 8
else:
    BITS = 7

decoded_text = ""
for line in lines:
    line = line.strip()
    if len(line) % BITS == 0 and len(line) > 0:
        for i in range(0, len(line), BITS):
            char_bin = line[i:i+BITS]
            char = chr(int(char_bin, 2))
            #added this from chat gpt - works to handle backspaces, tabs, and \n
            if char == "\b" or ord(char) == 8:  # Handle backspace by removing last character
                decoded_text = decoded_text[:-1]
            elif char == "\t" or ord(char) == 9:  # Handle tab character
                decoded_text += "\t"
            elif ord(char) == 10:  # Handle new line character
                decoded_text += "\n"
            else:
                decoded_text += char
        decoded_text += "\n"  
    else:
        print("Decoding failed")


if decoded_text:
    print(decoded_text)


with open("chaloutput.txt", "w") as output_file:
    output_file.write(decoded_text)
    print("Done")