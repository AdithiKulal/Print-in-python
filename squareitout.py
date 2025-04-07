def square_numbers(start, end):
    squares = [i**2 for i in range(start, end+1)]
    odd_squares = [num for num in squares if num % 2 != 0]
    even_squares = [num for num in squares if num % 2 == 0]
    return squares, odd_squares, even_squares

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

all_squares, odd_squares, even_squares = square_numbers(start_range, end_range)

print("All Squares:", all_squares)
print("Odd Squares:", odd_squares)
print("Even Squares:", even_squares)
