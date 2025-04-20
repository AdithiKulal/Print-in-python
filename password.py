import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits
    
    # Generate a password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Ensure the password has at least one lower case letter, one upper case letter, and one digit
    while not (any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
        password = ''.join(random.choice(characters) for _ in range(length))
    
    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

def main():
    length = int(input("Enter the length of the password: "))
    if length < 3:
        print("Password length should be at least 3.")
    else:
        password = generate_password(length)
        print("Generated Password : ", password)

if __name__ == "__main__":
    main()
