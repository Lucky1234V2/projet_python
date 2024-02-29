import tkinter as tk
from tkinter import messagebox

from minimax_algorithm import find_best_move


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.current_player = 'X'
        self.size = 8
        self.gui = TicTacToeGUI(self)
        self.gui.start()

    def is_winner(self, player):
        # Vérifier les lignes
        for row in self.board:
            for i in range(5):
                if all(cell == player for cell in row[i:i+4]):
                    return True

        # Vérifier les colonnes
        for col in range(8):
            for row in range(5):
                if all(self.board[row+i][col] == player for i in range(4)):
                    return True

        # Vérifier les diagonales (de haut gauche à bas droite)
        for row in range(5):
            for col in range(5):
                if all(self.board[row+i][col+i] == player for i in range(4)):
                    return True

        # Vérifier les diagonales (de bas gauche à haut droite)
        for row in range(3, 8):
            for col in range(5):
                if all(self.board[row-i][col+i] == player for i in range(4)):
                    return True

        return False

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def undo_move(self, row, col):
        self.board[row][col] = ' '
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' '

    def get_valid_moves(self):
        moves = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == ' ':
                    if any(self.board[r][c] != ' ' for r, c in self.get_neighbors(row, col)):
                        moves.append((row, col))
        return moves

    def get_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            if 0 <= row + dr < self.size and 0 <= col + dc < self.size:
                yield row + dr, col + dc

    def is_game_over(self):
        return self.check_win('X') or self.check_win('O') or all(self.board[row][col] != ' ' for row in range(self.size) for col in range(self.size))

    def check_win(self, player):
        for row in range(self.size):
            for col in range(self.size):
                if any(self.check_line(row, col, dr, dc, player) for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]):
                    return True
        return False

    def check_line(self, row, col, dr, dc, player):
        count = 0
        for _ in range(4):
            if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == player:
                count += 1
                row += dr
                col += dc
            else:
                break
        return count == 4

    def get_game_over_message(self):
        if self.check_win('X'):
            return "Player X wins!"
        elif self.check_win('O'):
            return "Player O wins!"
        else:
            return "The game is a tie!"


class TicTacToeGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.board_buttons = []
        self.create_board()

    def create_board(self):
        for row in range(8):
            button_row = []
            for col in range(8):
                button = tk.Button(self.root, text=" ", width=4, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.board_buttons.append(button_row)

    def make_move(self, row, col):
        if self.game.is_valid_move(row, col):
            self.game.make_move(row, col)
            self.update_board()
            if self.game.is_game_over():
                self.show_result()
            else:
                self.update_turn_label()
                self.make_ai_move()

    def update_board(self):
        for row in range(8):
            for col in range(8):
                self.board_buttons[row][col]['text'] = self.game.board[row][col]

    def update_turn_label(self):
        current_player = "Player X" if self.game.current_player == 'X' else "Player O"
        self.root.title(f"Tic Tac Toe - {current_player}'s turn")

    def make_ai_move(self):
        if self.game.current_player == 'O':
            move = find_best_move(self.game)
            if move:
                row, col = move
                self.game.make_move(row, col)
                self.update_board()
                if self.game.is_game_over():
                    self.show_result()
                else:
                    self.update_turn_label()

    def show_result(self):
        result = self.game.get_game_over_message()
        messagebox.showinfo("Game Over", result)
        self.root.quit()

    def start(self):
        self.update_turn_label()
        self.root.mainloop()


if __name__ == "__main__":
    TicTacToe()
