def generate_odd_even(n):
    odd_numbers = [i for i in range(n) if i % 2 != 0]
    even_numbers = [i for i in range(n) if i % 2 == 0]
    return odd_numbers, even_numbers

def capitalize_fruits(fruits):
    capitalized_fruits = [fruit.capitalize() for fruit in fruits]
    return capitalized_fruits

def main():
    n = int(input("Enter a number: "))
    odd, even = generate_odd_even(n)
    print("Odd numbers:", odd)
    print("Even numbers:", even)

    fruits = ["apple", "banana", "cherry", "date"]
    capitalized = capitalize_fruits(fruits)
    print("Original Fruits:", fruits)
    print("Capitalized Fruits:", capitalized)

if __name__ == "__main__":
    main()
