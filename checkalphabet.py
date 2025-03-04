char=input("Enter a character: ")
if('a'<=char<='z')or('A'<=char<='Z'):
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is not an alphabet")
    print("WARNING: this character is inappropriate. Please enter a correct character")
