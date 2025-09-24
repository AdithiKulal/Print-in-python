import tkinter as tk
import random

window = tk.Tk()
window.geometry("400x400")
window.title("Rock Paper Scissors Game")

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def play(user_choice):
    computer_choice = get_computer_choice()
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

title_label = tk.Label(window, text="Rock Paper Scissors Game", font=("Arial", 16))
title_label.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('Rock'))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('Paper'))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('Scissors'))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

result_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

window.mainloop()