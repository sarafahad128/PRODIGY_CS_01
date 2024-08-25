#create a function that takes text, shift(key) and mode(encrypt/decrpyt) to apply on the text
def caesar_cipher(text, shift, mode):
    result = ""
    # Adjust shift for decryption
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result
#main menu for user
def main():
    print("Caesar Cipher")
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode")
        return
    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
