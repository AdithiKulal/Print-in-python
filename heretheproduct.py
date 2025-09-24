import tkinter as tk

def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, f"Product: {product}")

window = tk.Tk()
window.geometry("400x300")
window.title("Getting Started with Widgets")

desc_label = tk.Label(window, text="This app multiplies two numbers", font=("Arial", 12), fg="blue")
desc_label.pack(pady=10)

frame = tk.Frame(window)
frame.pack(pady=10)

label1 = tk.Label(frame, text="Enter first number:", font=("Arial", 12))
label1.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame, font=("Arial", 12))
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(frame, text="Enter second number:", font=("Arial", 12))
label2.grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame, font=("Arial", 12))
entry2.grid(row=1, column=1, padx=5, pady=5)

calc_btn = tk.Button(window, text="Calculate Product", font=("Arial", 12), bg="#FFB6C1", command=calculate_product)
calc_btn.pack(pady=10)

result_box = tk.Text(window, height=2, width=30, font=("Arial", 12))
result_box.pack(pady=10)

window.mainloop()