import hashlib

# Function to create a new user account
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open("user_data.txt", "a") as file:
        file.write(f"{username}:{hashed_password}\n")

    print("Registration successful!")

# Function to authenticate a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Hash the entered password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open("user_data.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and hashed_password == stored_password:
                return True

    return False

# Secured page accessible to authenticated users
def secured_page():
    print("Welcome to the secured page!")
    # Add your secured page content here

# Main program loop
while True:
    print("\nOptions:")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Select an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        if login():
            secured_page()
        else:
            print("Login failed. Please try again.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
