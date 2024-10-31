import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [None] * 9

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda idx=i: self.make_move(idx))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, idx):
        if not self.board[idx]:
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif all(self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]]:
                return True
        return False

    def reset_game(self):
        self.board = [None] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
