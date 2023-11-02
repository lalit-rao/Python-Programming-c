def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        if char.islower():
            encrypted_char = chr(((ord(char) - ord('a') - 2) % 26) + ord('a'))
        elif char.isupper():
            encrypted_char = chr(((ord(char) - ord('A') - 3) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message


input_message = input("Enter a message: ")
encrypted_result = encrypt_message(input_message)
print(encrypted_result)
