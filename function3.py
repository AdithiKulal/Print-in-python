def add(P, Q):
  return P+Q
def subtract (P, Q):
  return P -Q
def multiply(P, Q):
  return P * Q
def divide(P, Q):
  return P / Q
print("Please select your desired operatio: ")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
choice=input("Please enter your option(a/b/c/d): ")
num_1=int(input("Enter the first number: "))
num_2=int(input("Enter the second number: "))
if choice == 'a':
  print(num_1, "+", num_2,"=",add(num_1, num_2))
elif choice == 'b':
  print(num_1, "-", num_2,"=",subtract(num_1, num_2))
elif choice == 'c':
  print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice == 'd':
  print(num_1,"/", num_2,"=",divide(num_1,num_2))
else:
  print("This is an invalid input")