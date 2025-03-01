decimal_number = int(input("Enter a decimal number: "))
binary_number = ""

while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number = decimal_number // 2

print("The binary representation is: ",binary_number)