from password_manager import (
    encrypt_passwords_in_file,
    change_password,
    add_login
)

def main():
    # Paso 1: pedir archivo
    print("Enter the CSV file name:")
    filename = input()

    # Encriptar todas las contraseñas del archivo
    encrypt_passwords_in_file(filename)

    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        option = input()

        # OPCIÓN 1: Cambiar contraseña
        if option == "1":
            print("Enter the website and the new password:")
            user_input = input().split()

            if len(user_input) < 2:
                print("Input is in the wrong format!")
                continue

            website, password = user_input

            if len(password) < 12:
                print("Password is too short!")
                continue

            success = change_password(filename, website, password)

            if not success:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")

        # OPCIÓN 2: Agregar login
        elif option == "2":
            print("Enter the website, username, and password:")
            user_input = input().split()

            if len(user_input) < 3:
                print("Input is in the wrong format!")
                continue

            website, username, password = user_input

            if len(password) < 12:
                print("Password is too short!")
                continue

            add_login(filename, website, username, password)
            print("Login added.")

        # OPCIÓN 3: Salir
        elif option == "3":
            break

        # OPCIÓN INVÁLIDA
        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()