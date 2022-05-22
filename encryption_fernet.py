from cryptography.fernet import Fernet

sel = int(input("Would you like to  create a new key, encrypt or decrypt? (0 = create key , 1 = encrypt, 2 = decrypt) "))

if sel == 0:
    key = Fernet.generate_key()
    print("YOUR KEY: ")
    print(key)
    with open('thekey.txt', 'wb') as file:
        file.write(key)

if sel == 1:
    inp2 = input("path to key file ").encode('utf-8')
    with open(inp2, 'rb') as file:
        key = file.readline()
    f = Fernet(key)

    text = int(input("do you want to encode a file or plaintext (0 = file, 1 = plaintext) :"))

    if text == 0:
        print("naj!")
    elif text == 1:
        inp = input("Enter Text: ").encode('utf-8')  # Type here
        encoded = f.encrypt(inp)
        text2 = input("What do you want to call the outfile ?")
        with open(text2, 'wb') as file:
            file.write(encoded)
elif sel == 2:
    inp2 = input("path to key file ").encode('utf-8')
    with open(inp2, 'rb') as file:
        key = file.readline()
    f = Fernet(key)

    inp3 = input("path to encoded file ").encode('utf-8')
    with open(inp3, 'rb') as file:
        encoded = file.readline()
    out = f.decrypt(encoded)
    print(out)



