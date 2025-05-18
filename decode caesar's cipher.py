print("This program decrypts a message using ceasar's cipher")
message = input("Enter coded message: ")
shift = int(input("Enter the number of times it was shifted: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for char in message:
    if char.lower() in alphabet:
        is_upper = char.isupper()
        index = alphabet.index(char.lower())
        new_index = (index - shift) % 26
        new_char = alphabet[new_index]
        if is_upper:
            new_char = new_char.upper()
        result += new_char
    else:
        result += char 

print("Decoded message:", result)
