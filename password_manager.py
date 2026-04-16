import csv
 
from caesar import caesar_encrypt
 
 
def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, 'r') as file:
        password = file.read().strip()
   
    encrypted = caesar_encrypt(password)
   
    with open(filename, 'w') as file:
        file.write(encrypted)
    pass
 
def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    import csv
 
def encrypt_passwords_in_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
       
        for row in reader:
            print(row)
 
import csv
 
def encrypt_passwords_in_file(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
       
        for row in reader:
            print(row)
 
import csv
from caesar import caesar_encrypt
 
def encrypt_passwords_in_file(filename):
   
   
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row]  # evita filas vacías
 
   
   
    for i in range(1, len(rows)):  # empezamos en 1 para NO tocar encabezado
        password = rows[i][2]
        rows[i][2] = caesar_encrypt(password)
 
   
   
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    pass
 
 
def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
 
import csv
 
from caesar import caesar_encrypt
 
def change_password(filename, website, password):
    # Leer todas las filas (evitando vacías)
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row]
 
    found = False
 
    for i in range(1, len(rows)):  
        if rows[i][0] == website:
            rows[i][2] = caesar_encrypt(password)
            found = True
            break
 
   
    if not found:
        return False
 
   
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
 
    return True
    pass
 
 
def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    import csv
from caesar import caesar_encrypt
 
def add_login(filename, website_name, username, password):
    # Encriptar la contraseña
    encrypted_password = caesar_encrypt(password)
   
    # Agregar nueva fila al CSV
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website_name, username, encrypted_password])
    pass
 
 