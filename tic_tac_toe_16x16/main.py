import tkinter as tk

from game_logic import TicTacToeGame
from minimax_algorithm import find_best_move


class TicTacToeApp:
    def __init__(self, root):
        self.game = TicTacToeGame(size=16)
        self.root = root
        self.buttons = [[None for _ in range(16)] for _ in range(16)]
        self.initialize_ui()

    def initialize_ui(self):
        for i in range(16):
            for j in range(16):
                b = tk.Button(self.root, text=' ', font=('Arial', 12), height=2, width=4,
                              command=lambda row=i, col=j: self.player_move(row, col))
                b.grid(row=i, column=j)
                self.buttons[i][j] = b

    def player_move(self, row, col):
        if self.game.make_move(row, col):
            self.buttons[row][col]['text'] = self.game.current_player
            self.game.switch_player()
            if self.game.check_win(row, col):
                self.end_game(f"{self.game.current_player} wins!")
            else:
                self.ai_move()

    def ai_move(self):
        row, col = find_best_move(self.game)
        if self.game.make_move(row, col):
            self.buttons[row][col]['text'] = self.game.current_player
            self.game.switch_player()
            if self.game.check_win(row, col):
                self.end_game(f"{self.game.current_player} wins!")

    def end_game(self, message):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")
        end_window = tk.Toplevel(self.root)
        end_window.title("Game Over")
        tk.Label(end_window, text=message, font=('Arial', 20)).pack(pady=20)
        tk.Button(end_window, text="Close",
                  command=self.root.destroy).pack(pady=20)


def main():
    root = tk.Tk()
    root.title("Tic Tac Toe 16x16")
    app = TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
