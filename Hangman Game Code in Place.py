import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
word = random.choice(word_list)
guessed = ["_"] * len(word)
attempts = 6

# Initialize the main window
root = tk.Tk()
root.title("Hangman Game")

# Create a canvas for drawing the hangman
canvas = tk.Canvas(root, width=200, height=250)
canvas.pack()

# Function to draw the hangman step by step
def draw_hangman(attempts_left):
    canvas.delete("hangman_part")  # Clear the previous hangman drawing
    if attempts_left <= 5:
        canvas.create_line(50, 200, 150, 200, tag="hangman_part")  # Base
    if attempts_left <= 4:
        canvas.create_line(100, 200, 100, 50, tag="hangman_part")  # Stand
    if attempts_left <= 3:
        canvas.create_line(100, 50, 150, 50, tag="hangman_part")  # Top
    if attempts_left <= 2:
        canvas.create_line(150, 50, 150, 70, tag="hangman_part")  # Noose
    if attempts_left <= 1:
        canvas.create_oval(140, 70, 160, 90, tag="hangman_part")  # Head
    if attempts_left == 0:
        canvas.create_line(150, 90, 150, 130, tag="hangman_part")  # Body
        canvas.create_line(150, 100, 140, 110, tag="hangman_part")  # Left arm
        canvas.create_line(150, 100, 160, 110, tag="hangman_part")  # Right arm
        canvas.create_line(150, 130, 140, 150, tag="hangman_part")  # Left leg
        canvas.create_line(150, 130, 160, 150, tag="hangman_part")  # Right leg

# Function to update the display after each guess
def update_display():
    display = " ".join(guessed)
    lbl_word.config(text=display)
    draw_hangman(attempts)

# Function to check the guess and update the game state
def check_guess():
    global word, guessed, attempts
    guess = entry_guess.get().lower()
    entry_guess.delete(0, tk.END)

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                guessed[index] = guess
        update_display()
        if "_" not in guessed:
            messagebox.showinfo("Hangman", "You won!")
            reset_game()
    else:
        attempts -= 1
        update_display()
        if attempts == 0:
            messagebox.showinfo("Hangman", "Game over! The word was " + word)
            reset_game()

# Function to reset the game
def reset_game():
    global word, guessed, attempts
    word = random.choice(word_list)
    guessed = ["_"] * len(word)
    attempts = 6
    update_display()

# Create the UI elements
lbl_word = tk.Label(root, text=" ".join(guessed), font=('Helvetica', 18))
lbl_word.pack()

entry_guess = tk.Entry(root)
entry_guess.pack()

btn_check = tk.Button(root, text="Guess", command=check_guess)
btn_check.pack()

# Start the game
update_display()
root.mainloop()
