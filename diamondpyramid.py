print("Diamond pattern of stars is:(*)")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()
