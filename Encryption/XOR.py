# XOR = Text ^ Key = crypt
# crypt ^ key = Decrypt

# Before optimization

# def isXOR(txt, encrypt):
#     newText = []
#     for c in txt:
#         newText.append(ord(c) ^ encrypt)
#     return ''.join(chr(n) for n in newText)

# Optimized

def isXOR(txt, encrypt):
    return ''.join(chr(ord(c) ^ encrypt) for c in txt)

while True:
    print("\n=== XOR Menu ===")
    print("1. Encrypt a text")
    print("2. Decrypt the last encrypted text")
    print("3. Quit")

    choice = input("Choose an option : ")

    if choice == "1":
        txt = input("Text to encrypt : ")
        key = int(input("Key for the encryption (0-255) : "))
        cipher = isXOR(txt, key)
        print("\nEncrypted text : ", cipher)

    elif choice == "2":
        if cipher is None:
            print("\nNothing to decrypt! You must encrypt something first.")
        else:
            result = isXOR(cipher, key)
            print("\nCrypted text : ", cipher)
            print("\nDecrypted text : ", result)

    elif choice == "3":
        print("Finished")
        break

    else:
        print("\nInvalid choice, try again.")