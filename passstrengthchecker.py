import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        strength = "Weak"
        color = "red"
    elif 6 <= length <= 8:
        strength = "Medium"
        color = "yellow"
    elif 9 <= length <= 12:
        strength = "Strong"
        color = "light green"
    else:
        strength = "Very Strong"
        color = "dark green"

    result_label.config(text=f"Strength: {strength}", fg=color)

window = tk.Tk()
window.geometry("400x400")
window.title("Password Strength Checker App")

title_label = tk.Label(window, text="Enter Your Password", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(window, show="*", font=("Arial", 12), width=30)
entry.pack(pady=10)

check_btn = tk.Button(window, text="Check Strength", font=("Arial", 12), bg="#add8e6", command=check_strength)
check_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)

window.mainloop()