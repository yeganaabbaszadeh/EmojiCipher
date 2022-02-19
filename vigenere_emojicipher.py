symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

emojis = ["\U0001F600", "\U0001F601", "\U0001F602", "\U0001F603", "\U0001F604", "\U0001F605", "\U0001F606", "\U0001F607", "\U0001F608", "\U0001F609", "\U0001F610", "\U0001F611", "\U0001F612", "\U0001F613", "\U0001F614", "\U0001F615", "\U0001F616", "\U0001F617", "\U0001F618", "\U0001F619", "\U0001F620", "\U0001F621", "\U0001F622","\U0001F623", "\U0001F624", "\U0001F625", "\U0001F626", "\U0001F627", "\U0001F628", "\U0001F629", "\U0001F630", "\U0001F631", "\U0001F632", "\U0001F633", "\U0001F634", "\U0001F635", "\U0001F636", "\U0001F637", "\U0001F638", "\U0001F639", "\U0001F640", "\U0001F641", "\U0001F642", "\U0001F643", "\U0001F644", "\U0001F645", "\U0001F646","\U0001F647", "\U0001F648", "\U0001F649", "\U0001F360", "\U0001F361", "\U0001F362", "\U0001F363", "\U0001F364", "\U0001F365", "\U0001F366", "\U0001F367", "\U0001F368", "\U0001F369", "\U0001F370", "\U0001F371"]

cell_num = len(symbols)

matrix_table = [[0] * cell_num for i in range(cell_num)]
x = 0
for i in range(0, cell_num):
    for j in range(0, cell_num):
        matrix_table[i][j] = emojis[(j+x) % len(symbols)]
    x += 1


def generateKey(text, key):
    key = list(key)
    if len(text) == len(key):
        return(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


def encrypt(plaintext, key):
    ciphertext = ''
    for i in range(0, len(plaintext)):
        if (plaintext[i].isalpha() or plaintext[i].isdigit()):
            ciphertext += matrix_table[symbols.index(plaintext[i])][symbols.index(key[i])]
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ''
    for i in range(0, len(ciphertext)):
        if (not ciphertext[i].isascii()):
            for j in range(0, len(symbols)):
                char = matrix_table[j][symbols.index(key[i])]
                if char == ciphertext[i]:
                    plaintext += symbols[j]
                    continue
        else:
            plaintext += ciphertext[i]
            continue
    return plaintext


def main():
    print("Welcome to Emoji Cipher!")

    while True:
        option = input(
            "Choose the operation ('e' for encryption, 'd' for decryption, 'q' for quit): ").lower()

        if option == 'e':
            message = input("Enter the message to encrypt: ")
            keyword = input("Enter the key: ").upper()
            key = generateKey(message, keyword)
            print("Here is your encrypted message:", encrypt(message, key))

        elif option == 'd':
            message = input("Enter the message to decrypt: ")
            keyword = input("Enter the key: ").upper()
            key = generateKey(message, keyword)
            print("Here is your decrypted message:", decrypt(message, key))

        elif option == 'q':
            print("Bye!")
            quit()

        else:
            print("Invalid option! Please try again.")
            continue


if __name__ == "__main__":
    main()
