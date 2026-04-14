# FREEZE CODE BEGIN
def caesar_encrypt(text: str, shift: int = 3) -> str:
    """Encrypts only letters using a Caesar cipher, leaving numbers and symbols unchanged."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Encrypt only alphabetic characters
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        elif char.isdigit():  # Encrypt digits
            encrypted_text += chr(((ord(char) - ord('0') + shift) % 10) + ord('0'))
        else:
            encrypted_text += char  # Keep numbers and symbols unchanged
    return encrypted_text

# FREEZE CODE END