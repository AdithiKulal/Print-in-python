number = int(input("Enter a number: "))
count = 0

while number > 0:
    remainder = number % 10
    print(remainder, end=" ")
    number = number // 10
    count += 1 