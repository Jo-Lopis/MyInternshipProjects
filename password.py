import random
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    # Define character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    print("----------------------------------------")

    try:
        length = int(input("Enter the length of the password (default is 8): ") or 8)
        count = int(input("Enter the number of passwords to generate: "))

        if length < 8 or count <= 0:
            print("Password length must be at least 8 characters, and count must be greater than 0.")
            return

        passwords = [generate_password(length) for _ in range(count)]

        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()