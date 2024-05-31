import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the length.")
                continue
            password = generate_password(length)
            print(f"Generated password: {password}")
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
