name=input("Enter the student's name: ")
age=int(input("Enter the student's age: "))
if age >= 10:
    if age <=20:
        print(f"Welcome, {name}! You are eligible to join the class.")
    else:
        print(f"Sorry, {name}. You are too old to join the class.")
else:
    print(f"Sorry, {name}. You are too young to join the class.") 
    print("Congratulations!", name)