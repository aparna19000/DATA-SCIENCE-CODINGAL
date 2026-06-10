import tkinter as tk
import random

# Choices available
choices = ["Rock", "Paper", "Scissors"]

# Function to play the game
def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

# Heading
title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16))
title.pack(pady=10)

# Instruction
instruction = tk.Label(root, text="Choose Rock, Paper, or Scissors")
instruction.pack()

# Buttons
rock_btn = tk.Button(root, text="Rock", width=10,
                     command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=10,
                      command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=10,
                         command=lambda: play("Scissors"))
scissors_btn.pack(pady=5)

# Computer Choice Label
computer_label = tk.Label(root, text="")
computer_label.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Run GUI
root.mainloop()