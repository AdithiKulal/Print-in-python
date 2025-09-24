import tkinter as tk

def calculate_interest():
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    si = (p * t * r) / 100
    ci = p * ((1 + r / 100) ** t) - p

    result_label.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}")

window = tk.Tk()
window.geometry("400x400")
window.title("Interest Calculator App")

frame = tk.Frame(window)
frame.pack(pady=20)

tk.Label(frame, text="Principal:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
principal_entry = tk.Entry(frame, font=("Arial", 12))
principal_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Time (years):", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
time_entry = tk.Entry(frame, font=("Arial", 12))
time_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Rate (%):", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
rate_entry = tk.Entry(frame, font=("Arial", 12))
rate_entry.grid(row=2, column=1, padx=5, pady=5)

calc_btn = tk.Button(window, text="Calculate", font=("Arial", 12), bg="#87CEFA", command=calculate_interest)
calc_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14), fg="green")
result_label.pack(pady=20)

window.mainloop()