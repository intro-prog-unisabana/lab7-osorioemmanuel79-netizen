from password_manager import add_login, change_password, encrypt_passwords_in_file
 
 
def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
    from password_manager import encrypt_passwords_in_file, change_password, add_login
 
def main():
   
    filename = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(filename)
 
    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        option = input()
 
        if option == "1":
            print("Enter the website and the new password:")
            user_input = input().split()
 
            if len(user_input) < 2:
                print("Input is in the wrong format!")
                continue
 
            website, new_password = user_input
 
            if len(new_password) < 12:
                print("Password is too short!")
                continue
 
            success = change_password(filename, website, new_password)
 
            if not success:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")
 
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
 
        elif option == "3":
            break
 
        else:
            print("Invalid option selected!")
    pass
 
 
if __name__ == "__main__":
    main()