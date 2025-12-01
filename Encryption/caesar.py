# check https://en.wikipedia.org/wiki/Caesar_cipher

alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt (passwd, dec):
    Crypted = ""
    for ltr in passwd:
        if ltr in alpha:
            position = alpha.index(ltr)
            newPos = (position + dec) % 26
            Crypted += alpha[newPos]
        elif ltr.lower() in alpha:
            position = alpha.index(ltr.lower())
            newPos = (position + dec) % 26
            Crypted += alpha[newPos].upper()
        else:
            Crypted += ltr
    return Crypted

def decrypt (passwd, dec):
    Crypted = ""
    for ltr in passwd:
        if ltr in alpha:
            position = alpha.index(ltr)
            newPos = (position - dec) % 26
            Crypted += alpha[newPos]
        elif ltr.lower() in alpha:
            position = alpha.index(ltr.lower())
            newPos = (position - dec) % 26
            Crypted += alpha[newPos].upper()
        else:
            Crypted += ltr
    return Crypted

choice = int(input("Please choose between 1 --> Encrypt or 2 --> Decrypt : "))

if choice == 1:
    passwd = input("Enter a password : ")
    dec = int(input("Enter the number for the encryption : "))
    print("Encrypted : ", encrypt(passwd, dec))
elif choice == 2:
    passwd = input("Enter a password : ")
    dec = int(input("Enter the number for the encryption : "))
    print("Decrypted : ", decrypt(passwd, dec))
else:
    print("Invalid choice")