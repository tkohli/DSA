

def encode_string(input_string, shift):
    encoded_string = ""
    for char in input_string:
        if char.isdigit():
            encoded_char = str((int(char) + shift + 1) % 10)
            
        elif char.isalpha():
            encoded_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            if char.islower():
                encoded_char = encoded_char.lower()
        else:
            encoded_char = char
        encoded_string += encoded_char
    return encoded_string

# Example usage
input_str = "CiscO123"
encoded_str = encode_string(input_str,-1)
print(encoded_str)