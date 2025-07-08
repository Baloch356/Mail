import re
import secrets
import string

def get_account_type():
    while True:
        choice = input("Please select the type of account to create: (1) for UK, (2) for USA: ")
        if choice == '1':
            return 'UK'
        elif choice == '2':
            return 'USA'
        else:
            print("Invalid choice. Please enter 1 or 2.")

def get_date_of_birth():
    while True:
        dob_str = input("Please enter the date of birth (YYYY-MM-DD). For example, to be over 18, you could use 1999-01-01: ")
        if re.match(r'^\d{4}-\d{2}-\d{2}$', dob_str):
            return dob_str
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_email_address():
    while True:
        email = input("Please enter the email address for the new account: ")
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return email
        else:
            print("Invalid email format. Please enter a valid email address.")

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def get_password_option():
    while True:
        choice = input("Do you want to (1) enter a custom password or (2) have one auto-generated?: ")
        if choice == '1':
            return 'custom'
        elif choice == '2':
            return 'auto'
        else:
            print("Invalid choice. Please enter 1 or 2.")

def get_password():
    password_option = get_password_option()
    if password_option == 'custom':
        password = input("Please enter your custom password: ")
        return password
    else:
        generated_password = generate_strong_password()
        print(f"Auto-generated password: {generated_password}")
        return generated_password

if __name__ == "__main__":
    print("Starting account creation bot...")
    
    account_type = get_account_type()
    date_of_birth = get_date_of_birth()
    email_address = get_email_address()
    password = get_password()
    
    print("\n--- Collected Information ---")
    print(f"Account Type: {account_type}")
    print(f"Date of Birth: {date_of_birth}")
    print(f"Email Address: {email_address}")
    print(f"Password: {password}")
    print("-----------------------------")

