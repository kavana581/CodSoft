import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle the user's selection and computer's random choice
def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    # Display choices
    label_user_choice.config(text=f"Your choice: {user_choice}")
    label_computer_choice.config(text=f"Computer's choice: {computer_choice}")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)

    # Display the result
    label_result.config(text=f"Result: {result}")

    # Update the score
    if result == "You win!":
        global user_score
        user_score += 1
        label_user_score.config(text=f"Your score: {user_score}")
    elif result == "You lose!":
        global computer_score
        computer_score += 1
        label_computer_score.config(text=f"Computer's score: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_user_score.config(text="Your score: 0")
    label_computer_score.config(text="Computer's score: 0")
    label_user_choice.config(text="Your choice: ")
    label_computer_choice.config(text="Computer's choice: ")
    label_result.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("450x500")  # Adjusted to accommodate buttons and labels
root.config(bg="#f0f8ff")  # Set background color

# Initialize scores
user_score = 0
computer_score = 0

# Title Label - Main Title with bigger font
label_title = tk.Label(root, text="Rock-Paper-Scissors Game", font=('Arial', 20, 'bold'), bg="#f0f8ff", fg="#333")
label_title.pack(pady=20)

# User Score Label
label_user_score = tk.Label(root, text="Your score: 0", font=('Arial', 12), bg="#f0f8ff", fg="#333")
label_user_score.pack()

# Computer Score Label
label_computer_score = tk.Label(root, text="Computer's score: 0", font=('Arial', 12), bg="#f0f8ff", fg="#333")
label_computer_score.pack()

# Buttons for Rock, Paper, Scissors with more vibrant colors
button_rock = tk.Button(root, text="Rock", font=('Arial', 14), width=15, height=2, command=lambda: play_game("Rock"), bg="#ff5733", fg="white", relief="raised")
button_rock.pack(pady=10)

button_paper = tk.Button(root, text="Paper", font=('Arial', 14), width=15, height=2, command=lambda: play_game("Paper"), bg="#33c6ff", fg="white", relief="raised")
button_paper.pack(pady=10)

button_scissors = tk.Button(root, text="Scissors", font=('Arial', 14), width=15, height=2, command=lambda: play_game("Scissors"), bg="#ffb733", fg="white", relief="raised")
button_scissors.pack(pady=10)

# Labels to display choices and result
label_user_choice = tk.Label(root, text="Your choice: ", font=('Arial', 12), bg="#f0f8ff", fg="#333")
label_user_choice.pack(pady=5)

label_computer_choice = tk.Label(root, text="Computer's choice: ", font=('Arial', 12), bg="#f0f8ff", fg="#333")
label_computer_choice.pack(pady=5)

label_result = tk.Label(root, text="Result: ", font=('Arial', 14, 'bold'), bg="#f0f8ff", fg="#333")
label_result.pack(pady=10)

# Button to reset the game with a bright color
button_reset = tk.Button(root, text="Reset Game", font=('Arial', 14), command=reset_game, bg="#d9534f", fg="white", relief="raised", width=15)
button_reset.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
