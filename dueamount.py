def calculate_change(total_bill,amount_paid):
    change=amount_paid-total_bill
    return change
total_bill=float(input("Enter the total bill(in decimal): ₹"))
amount_paid=float(input("Enter the amount paid(in decimal): ₹"))
change=calculate_change(total_bill,amount_paid)
if change > 0:
    print(f"The shopkeeper should return: ₹{change}")
else:
    print("No change")