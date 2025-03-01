print("Diamond pattern of numbers is:")
n = int(input("Enter the number of rows: "))

# Print the upper half of the diamond
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print(k + 1, end=" ")
    print()

# Print the lower half of the diamond
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print(k + 1, end=" ")
    print()