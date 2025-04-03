def check_age():
    while True:
        try:
            age=int(input("Enter your age:"))
            if age<0:
                print("Age cannot be negative. Please try again.")
            elif age>100:
                print("Age is not valid. Please try again!!")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid age.")
    if age%2==0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
check_age()