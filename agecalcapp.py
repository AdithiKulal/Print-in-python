import tkinter as tk
from datetime import date

def calculate_age():
    name = name_entry.get()
    d = int(day_entry.get())
    m = int(month_entry.get())
    y = int(year_entry.get())

    today = date.today()
    age = today.year - y - ((today.month, today.day) < (m, d))

    result_label.config(text=f"Hello {name}, you are {age} years old!")

window = tk.Tk()
window.geometry("400x400")
window.title("Age Calculator App")

frame = tk.Frame(window)
frame.pack(pady=20)

tk.Label(frame, text="Name:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Day:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
day_entry = tk.Entry(frame, font=("Arial", 12))
day_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Month:", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
month_entry = tk.Entry(frame, font=("Arial", 12))
month_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Year:", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
year_entry = tk.Entry(frame, font=("Arial", 12))
year_entry.grid(row=3, column=1, padx=5, pady=5)

calc_btn = tk.Button(window, text="Calculate Age", font=("Arial", 12), bg="#FFD700", command=calculate_age)
calc_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14), fg="green")
result_label.pack(pady=20)

window.mainloop()