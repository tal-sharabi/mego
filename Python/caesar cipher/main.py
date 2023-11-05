import graphics


def caesar_cipher(text, offset):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(((ord(char) - ord('a') + offset) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(((ord(char) - ord('A') + offset) % 26) + ord('A'))
        else:
            result += char
    return result


def main():
    while True:
        choice = input("Choose what you'd like to do:\nEncrypt (press 1)\nDecrypt (press 2)\n---> ")
        if choice == '1':
            text = input("Enter the text to encrypt: ")
            offset = int(input("OK, enter the offset >>> "))
            encrypted_text = caesar_cipher(text, offset)
            print(f"Encrypted sentence: {encrypted_text}")
        elif choice == '2':
            text = input("OK, enter the encrypted sentence >>> ")
            offset = int(input("Enter the offset >>> "))
            decrypted_text = caesar_cipher(text, -offset)
            print(f"Decrypted sentence: {decrypted_text}")

        continue_choice = input("Would you like to continue or quit? (C or Q)\n")
        if continue_choice.lower() != 'c':
            break


print("Welcome to the cypher program\n")
print(f"{graphics.logo}\n")
main()
