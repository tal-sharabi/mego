def caesar_cipher(text, offset, encrypt=True):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
        elif 'A' <= char <= 'Z':
            base = ord('A')
        else:
            result += char
            continue

        if encrypt:
            result += chr(((ord(char) - base + offset) % 26) + base)
        else:
            result += chr(((ord(char) - base - offset) % 26) + base)

    return result


def main():
    while True:
        choice = input("Choose what you'd like to do:\nEncrypt (press 1)\nDecrypt (press 2)\n---> ")

        if choice == '1':
            action = "encrypt"
        elif choice == '2':
            action = "decrypt"
        else:
            continue

        text = input(f"Enter the text to {action}: ")
        offset = int(input(f"OK, enter the offset >>> "))

        if choice == '1':
            result = caesar_cipher(text, offset)
        elif choice == '2':
            result = caesar_cipher(text, offset, encrypt=False)

        print(f"{action.capitalize()}ed sentence: {result}")

        continue_choice = input("Would you like to continue or quit? (C or Q)\n")
        if continue_choice.lower() != 'c':
            break


print("Welcome to the cypher program\n")
main()
