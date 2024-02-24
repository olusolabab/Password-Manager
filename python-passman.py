import hashlib
import getpass

passwordManager = {}

def createAccount():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    hashedPassword = hashlib.sha256(password.encode()).hexdigest()
    passwordManager[username] = hashedPassword
    print("Account created successfully!")


def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    hashedPassword = hashlib.sha256(password.encode()).hexdigest()
    if username in passwordManager.keys() and hashedPassword == passwordManager[username]:
        print("Login successful!")
    else:
        print("Invalid username or password.")


def main():
    while True:
        print("1. Create account")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            createAccount()
        elif choice == 2:
            login()
        elif choice == 3:
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

