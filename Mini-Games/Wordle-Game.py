import tkinter as tk
from tkinter import messagebox
import random

class CupGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cup Game")

        self.ball_position = random.randint(1, 3)

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Guess which cup has the ball!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.cup1_button = tk.Button(self.root, text="Cup 1", command=lambda: self.check_guess(1))
        self.cup1_button.pack(side=tk.LEFT, padx=20)

        self.cup2_button = tk.Button(self.root, text="Cup 2", command=lambda: self.check_guess(2))
        self.cup2_button.pack(side=tk.LEFT, padx=20)

        self.cup3_button = tk.Button(self.root, text="Cup 3", command=lambda: self.check_guess(3))
        self.cup3_button.pack(side=tk.LEFT, padx=20)

    def check_guess(self, guess):
        if guess == self.ball_position:
            messagebox.showinfo("Result", "You guessed right! The ball is under cup {}".format(guess))
        else:
            messagebox.showinfo("Result", "Wrong guess. The ball was under cup {}".format(self.ball_position))
        
        # Shuffle for the next round
        self.ball_position = random.randint(1, 3)

if __name__ == "__main__":
    root = tk.Tk()
    app = CupGameApp(root)
    root.mainloop()

