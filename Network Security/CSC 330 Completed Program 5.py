from ftplib import FTP

# FTP server details
IP = "10.0.222.38"
PORT = 33333
USER = "anonymous"
PASSWORD = "simple@abcdefg.com"
FOLDER = ""
USE_PASSIVE = True  # Set to False if the connection times out

# Connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# Navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.retrlines("LIST", files.append)  # Includes hidden files

# Exit the FTP server
ftp.quit()

# Sort files alphabetically by filename
files = sorted(files, key=lambda x: x[56:].lower())

# lines 31-36 were made with help from Christianna
binary_out = ""
for perms in files:
    permission_str = perms[:10]
    if BITS == 7:
        if permission_str[:3] == "---":  # ignore the distraction files
            binary_out += permission_str[3:10]
    elif BITS == 10:
        binary_out += permission_str[:10]

# replaces all values into binary
binary_out = binary_out.replace("-", "0")
binary_out = binary_out.replace("r", "1")
binary_out = binary_out.replace("w", "1")
binary_out = binary_out.replace("x", "1")
binary_out = binary_out.replace("d", "1")

print(binary_out)
