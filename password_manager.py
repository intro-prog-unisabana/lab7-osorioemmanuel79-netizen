from caesar import caesar_encrypt

def encrypt_single_pass(filename):
    # Leer la contraseña del archivo
    with open(filename, 'r') as file:
        password = file.read().strip()
    
    # Encriptar la contraseña
    encrypted_password = caesar_encrypt(password)
    
    # Sobrescribir el archivo con la contraseña encriptada
    with open(filename, 'w') as file:
        file.write(encrypted_password)