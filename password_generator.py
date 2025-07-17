import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return ""

    # All characters to use: letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("--- PASSWORD GENERATOR ---")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        if password:
            print(f"✅ Your generated password: {password}")
    except ValueError:
        print("❌ Please enter a valid number.")

# Run the main function
main()
