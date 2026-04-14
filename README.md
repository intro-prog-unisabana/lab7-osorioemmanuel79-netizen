[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/n9d4RRy-)
# Laboratorio 7: Gestor de Contraseñas Seguro usando E/S de Archivos y Encriptación en Python

## Objetivo

Eres la única persona de TI en una firma de ingeniería. Descubriste que todos los usuarios de la red corporativa tienen sus credenciales almacenadas en **texto plano** en archivos **CSV**. ¡Qué desastre! Esto es un enorme riesgo de seguridad para la empresa.

En este laboratorio, construirás un **gestor de contraseñas** que almacena contraseñas de forma "segura" usando un **cifrado César**. Desarrollarás progresivamente funciones que **encriptan contraseñas**, **leen y modifican entradas de contraseñas**, y **agregan nuevas credenciales de inicio de sesión**.

**Importante:** Para las partes 1-4, trabajarás **únicamente** en `password_manager.py`

---

## Parte 1: Encriptando una Contraseña Individual en un Archivo

Antes de trabajar con archivos CSV, primero encriptemos una **contraseña individual** almacenada en un archivo de texto.

### Tarea

Escribe una función `encrypt_single_pass(filename)` que:

1. **Lea una contraseña individual** de un archivo llamado `filename`.
2. Encripte la contraseña usando la función `caesar_encrypt` proporcionada. Impórtala desde `caesar.py`.
3. Escriba la **contraseña encriptada de vuelta al archivo**, sobrescribiendo la contraseña original.

### Pista

- Abre el archivo en **modo lectura** (`'r'`) para obtener la contraseña.
- Asegúrate de usar `strip()` en la contraseña para eliminar cualquier espacio en blanco circundante.
- Usa `caesar_encrypt(password)` para encriptarla.
- Abre el archivo en **modo escritura** (`'w'`) para guardar la contraseña encriptada en el archivo.

### Ejemplo

#### `example1.txt` Antes de la Llamada a la Función:

```plaintext
supersecure

```

#### Llamada a la Función:

```python
encrypt_single_pass('example1.txt')
```

#### `example1.txt` Después de la Llamada a la Función:

```plaintext
vxshuvhfxuh

```

## Parte 2: Encriptando Contraseñas en un Archivo CSV

### Subparte 2A: Leyendo el Archivo CSV

Ahora, comencemos a trabajar con un **archivo CSV** que contiene múltiples inicios de sesión.

El archivo CSV tiene el siguiente formato:

```plaintext
website,username,password
<sitio_web1>,<usuario1>,<contraseña1>
<sitio_web2>,<usuario2>,<contraseña2>
...
```

Nota que la primera línea contiene los nombres de las columnas, y cualquier línea posterior contiene los datos que te interesan.

### Tarea

1. Escribe una función `encrypt_passwords_in_file(filename)`. Por ahora, solo **leerá e imprimirá todas las entradas** del archivo CSV `filename`.

### Pista

- Abre el archivo usando `with open(filename, mode='r')`.
- Usa `csv.reader(file)` para analizar el archivo.
- Itera a través de las filas e imprime cada una.

### Ejemplo

#### `example2.csv`:

```plaintext
website,username,password
example.com,user123,password123
testsite.com,admin,letmein
mybank.com,johndoe,money2024
email.com,jane.doe,myemailpass

```

#### Salida Esperada:

```plaintext
['website', 'username', 'password']
['example.com', 'user123', 'password123']
['testsite.com', 'admin', 'letmein']
['mybank.com', 'johndoe', 'money2024']
['email.com', 'jane.doe', 'myemailpass']
```

Nota que la fila que contiene los títulos de las columnas se imprime. Manejaremos esto en la **Subparte 2B.**

---

### Subparte 2B: Encriptando Contraseñas en el Archivo CSV

Ahora, encriptemos **únicamente** las contraseñas en el archivo CSV mientras mantenemos el sitio web y el nombre de usuario sin cambios. Esto nos ayudará a solucionar nuestro problema de seguridad de contraseñas en texto plano.

### Tarea

1. Modifica la función de la **Subparte 2A** para encriptar **únicamente** la columna de contraseñas.
2. Escribe los datos actualizados **de vuelta al archivo**.

### Pista

- Lee todas las filas usando `csv.reader()`.
- Asegúrate de verificar que una línea tenga contenido. Si está en blanco, no la agregues a la lista.
- Convierte el resultado de `csv.reader()` en una lista que contenga todas las filas. Podrías usar una **comprensión de lista** para lograr esto.
- Modifica **únicamente** la tercera columna (`passwords`).
- Escribe los datos modificados de vuelta usando `csv.writer()` y usa el resultado `writer` para llamar `writer.writerows()`.

### Ejemplo

#### `example2.csv` Antes de la Llamada a la Función:

```plaintext
website,username,password
example.com,user123,password123
testsite.com,admin,letmein
mybank.com,johndoe,money2024
email.com,jane.doe,myemailpass

```

#### Llamada a la Función:

```python
encrypt_passwords_in_file('example2.csv')
```

#### `example2.csv` Después de la Llamada a la Función:

```plaintext
website,username,password
example.com,user123,sdvvzrug456
testsite.com,admin,ohwphlq
mybank.com,johndoe,prqhb5357
email.com,jane.doe,pbhpdlosdvv

```

## Parte 3: Cambiando una Contraseña en el Archivo CSV

Ahora que hemos encriptado todas las contraseñas, queremos facilitar a los usuarios **cambiar sus contraseñas** de forma segura para que no se frustren y vuelvan a usar texto plano.

### Tarea

1. Escribe una función `change_password(filename, website, password)` que:
   - Tome `website` y `password` como parámetros de tipo cadena.
   - Encuentre la fila correspondiente a `website` en el archivo CSV.
   - Si el nombre del sitio web no se encuentra, retorne `False` para indicar fallo.
   - De lo contrario, encripte la nueva `password`.
   - Actualice el archivo CSV con la nueva `password` encriptada.
   - Retorne `True` para indicar éxito.

### Pista

- Convierte el resultado de `csv.reader()` en una lista que contenga todas las filas.
- Asegúrate de verificar que una línea tenga contenido. Si está en blanco, no la agregues a la lista.
- Itera a través de la lista y encuentra el sitio web coincidente.
- Actualiza la columna de **contraseña** con la versión encriptada de la nueva contraseña.
- Escribe la lista actualizada de vuelta al archivo usando `csv.writer()` y `writer.writerows()`.
- En esta parte, recibirás archivos con las contraseñas ya encriptadas para probar tu código.

### Ejemplos

#### `example3.csv` Antes de la Llamada a la Función:

```plaintext
website,username,password
example.com,user123,sdvvzrug456
testsite.com,admin,ohwphlq
mybank.com,johndoe,prqhb5357
email.com,jane.doe,pbhpdlopdvv

```

#### Llamada a la Función:

```python
change_password("example3.csv", "testsite.com", "newsecurepass")
```

#### Valor de Retorno:

```python
True
```

#### `example3.csv` Después de la Llamada a la Función:

```plaintext
website,username,password
example.com,user123,sdvvzrug456
testsite.com,admin,qhzvhfxuhsdvv
mybank.com,johndoe,prqhb5357
email.com,jane.doe,pbhpdlopdvv

```

#### Llamada a Función Inválida (Sitio Web Faltante):

```python
change_password("example3.csv", "nonexistent.com", "randompass")
```

#### Valor de Retorno:

```python
False
```

## Parte 4: Agregando una Nueva Entrada

Ahora, permitamos a los usuarios agregar nuevos inicios de sesión.

### Tarea

1. Escribe una función `add_login(filename, website_name, username, password)` que:
   - Tome `filename`, `website_name`, `username` y `password` como parámetros.
   - Encripte la **contraseña**.
   - Anexe la nueva entrada al archivo CSV. Recuerda que el formato es:

   ```plaintext
   <nombre_sitio_web>,<usuario>,<contraseña>
   ```

### Pista

- Abre el archivo en **modo anexar** (`'a'`) para agregar una nueva entrada.
- Usa `csv.writer()` y `writer.writerow()` para escribir la nueva fila.
- En esta parte, recibirás archivos con las contraseñas ya encriptadas para probar tu código.

---

### Ejemplo

#### `example3.csv` Antes de la Llamada a la Función:

```plaintext
website,username,password
example.com,user123,sdvvzrug456
testsite.com,admin,qhzvhfxuhsdvv
mybank.com,johndoe,prqhb5357
email.com,jane.doe,pbhpdlopdvv

```

#### Llamada a la Función:

```python
add_login("example3.csv", "newsite.com", "newuser", "mypassword123")
```

#### `example3.csv` Después de la Llamada a la Función:

```plaintext
website,username,password
example.com,user123,sdvvzrug456
testsite.com,admin,qhzvhfxuhsdvv
mybank.com,johndoe,prqhb5357
email.com,jane.doe,pbhpdlopdvv
newsite.com,newuser,pbzdvvzrug456

```

## Parte 5: Escribiendo el Programa Principal

Ahora que todas las funciones auxiliares están listas, construyamos el **programa principal interactivo** para ayudar a los usuarios a gestionar sus contraseñas. Necesitarás importar tus funciones desde `password_manager.py` y escribir tu programa principal en `main.py`.

### Tarea

1. Pregunta al usuario por el **nombre del archivo CSV**, que actualmente contiene contraseñas en **texto plano**:

   ```plaintext
   Enter the CSV file name:
   ```

2. Encripta todas las contraseñas en texto plano del archivo usando una función de `password_manager.py`.

3. Entra en un **bucle** donde el usuario pueda:
   - Cambiar una contraseña.
   - Agregar un nuevo inicio de sesión.
   - Salir del programa.

     ```plaintext
     Options: (1) Change Password, (2) Add Password, (3) Quit:
     ```

   - Usarás el mismo archivo CSV que el usuario ingresa en el **Paso 1** para todas las operaciones que realices en el programa.

4. Si el usuario selecciona la opción `1`, pregunta al usuario por el nombre del sitio web para el cual quiere cambiar la contraseña y la nueva contraseña:

   ```plaintext
   Enter the website and the new password:
   ```

   - El usuario ingresará el sitio web y la nueva contraseña separados por un espacio.
   - Si el usuario ingresa menos de dos elementos separados por espacios, imprime:

     ```plaintext
     Input is in the wrong format!
     ```

     y regresa al menú principal.
   - Si la **contraseña** tiene menos de 12 caracteres, imprime:

     ```plaintext
     Password is too short!
     ```

     y regresa al menú principal.
   - De lo contrario, cambia la contraseña usando una función de `password_manager.py`.
   - Si la función que usaste para cambiar la contraseña retorna `False`, esto significa que la operación falló debido a que el sitio web no está en el archivo. Imprime el siguiente mensaje:

     ```plaintext
     Website not found! Operation failed.
     ```

   - De lo contrario (la función retornó `True`), imprime el siguiente mensaje:

     ```plaintext
     Password changed.
     ```

5. Si el usuario selecciona la opción `2`, pregunta al usuario por el nombre del sitio web, el nombre de usuario y la contraseña:

   ```plaintext
   Enter the website, username, and password:
   ```

   - El usuario ingresará el sitio web, nombre de usuario y contraseña separados por espacios.
   - Si el usuario ingresa menos de tres elementos separados por espacios, imprime:

     ```plaintext
     Input is in the wrong format!
     ```

     y regresa al menú principal.
   - Si la **contraseña** tiene menos de 12 caracteres, imprime:

     ```plaintext
     Password is too short!
     ```

     y regresa al menú principal.
   - De lo contrario, agrega el nuevo inicio de sesión usando una función de `password_manager.py` e imprime:

     ```plaintext
     Login added.
     ```

6. Si el usuario selecciona la opción `3`, sal del programa.

7. Si el usuario selecciona una opción inválida, imprime:

   ```plaintext
   Invalid option selected!
   ```

### Pista

- Usa `split()` para analizar la entrada del usuario separada por espacios.
- Puedes asumir que cada elemento de la entrada separada por espacios no contendrá espacios en sí mismo.

### Ejemplo

#### Archivo CSV Inicial `example4.csv`:

```plaintext
website,username,password
example.com,user123,password123
testsite.com,admin,testpassword
mybank.com,johndoe,bankpass123
email.com,jane.doe,emailpass456

```

#### Ejecución del Programa (E/S Estándar):

**Entrada:**

```plaintext
example4.csv
1
example.com newpassword123
2
newsite user123 newpassword123
1
testsite.com newtestpassword
4
3
```

**Salida:**

```plaintext
Enter the CSV file name:
Options: (1) Change Password, (2) Add Password, (3) Quit:
Enter the website and the new password:
Password changed.
Options: (1) Change Password, (2) Add Password, (3) Quit:
Enter the website, username, and password: 
Login added.
Options: (1) Change Password, (2) Add Password, (3) Quit:
Enter the website and the new password:
Password changed.
Options: (1) Change Password, (2) Add Password, (3) Quit:
Invalid option selected!
Options: (1) Change Password, (2) Add Password, (3) Quit:
```

---

#### Después de Encriptar las Contraseñas:

```
website,username,password
example.com,user123,sdvvqrzq456
testsite.com,admin,wkhvwhvshqg
mybank.com,johndoe,banksdvvv456
email.com,jane.doe,hphosqwvtyz
```

---

#### Después de Cambiar la Contraseña para `example.com`:

```
website,username,password
example.com,user123,sdvvqrzq456
testsite.com,admin,wkhvwhvshqg
mybank.com,johndoe,banksdvvv456
email.com,jane.doe,hphosqwvtyz
newsite,user123,sdvvqrzq456

```

---

#### Después de Agregar un Nuevo Inicio de Sesión para `newsite`:

```
website,username,password
example.com,user123,sdvvqrzq456
testsite.com,admin,wkhvwhvshqg
mybank.com,johndoe,banksdvvv456
email.com,jane.doe,hphosqwvtyz
newsite,user123,sdvvqrzq456

```

---

#### Después de Cambiar la Contraseña para `testsite.com`:

```
website,username,password
example.com,user123,sdvvqrzq456
testsite.com,admin,shqwhwhvwhg
mybank.com,johndoe,banksdvvv456
email.com,jane.doe,hphosqwvtyz
newsite,user123,sdvvqrzq456

```

---

#### Archivo CSV Final (después de salir):

```
website,username,password
example.com,user123,sdvvqrzq456
testsite.com,admin,shqwhwhvwhg
mybank.com,johndoe,banksdvvv456
email.com,jane.doe,hphosqwvtyz
newsite,user123,sdvvqrzq456

```
