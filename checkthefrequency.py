def check_frequency(test_dict, target_value):
    frequency = list(test_dict.values()).count(target_value)
    return frequency

test_dict = eval(input("Enter the dictionary (e.g., {'a': 1, 'b': 2, 'c': 1}): "))
target_value = input("Enter the value to check frequency: ")

try:
    target_value = int(target_value)
except ValueError:
    try:
        target_value = float(target_value)
    except ValueError:
        pass  
frequency = check_frequency(test_dict, target_value)
print(f"The frequency of {target_value} is: {frequency}")