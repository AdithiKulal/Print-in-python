import tkinter as tk

def convert_length():
    value = float(entry.get())
    converted = value * 100
    result_label.config(text=f"{value} meters = {converted} centimeters")

window = tk.Tk()
window.geometry("400x400")
window.title("Length Converter App")

title_label = tk.Label(window, text="Enter length in meters", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12), width=30)
entry.pack(pady=10)

convert_btn = tk.Button(window, text="Convert", font=("Arial", 12), bg="#90EE90", command=convert_length)
convert_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

window.mainloop()