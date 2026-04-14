import csv
from caesar import caesar_encrypt

def change_password(filename, website, password):
    rows = []
    found = False

    # Leer todo el archivo
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            # Evitar filas vacías
            if not row:
                continue
            
            # Buscar el sitio web (ignorando el encabezado)
            if row[0] == website:
                # Encriptar nueva contraseña
                row[2] = caesar_encrypt(password)
                found = True
            
            rows.append(row)

    # Si no se encontró el sitio
    if not found:
        return False

    # Escribir el archivo actualizado
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return True