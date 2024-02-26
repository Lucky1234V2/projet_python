class Game:
    def __init__(self, size=8):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = 'X'
        self.win_length = 4  # Nombre de symboles consécutifs nécessaires pour gagner

    def print_board(self):
        for row in self.board:
            print('|' + '|'.join(row) + '|')

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            return True
        return False

    def undo_move(self, row, col):
        self.board[row][col] = ' '

    def is_valid_move(self, row, col):
        return self.board[row][col] == ' '

    # Dans Game, ajoutez cette méthode pour obtenir tous les mouvements valides

    def get_valid_moves(self):
        valid_moves = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == ' ':
                    valid_moves.append((row, col))
        return valid_moves

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        # Vérifie toutes les rangées, colonnes et diagonales pour une victoire
        for row in range(self.size):
            if self.check_line_win([self.board[row][col] for col in range(self.size)]):
                return True
        for col in range(self.size):
            if self.check_line_win([self.board[row][col] for row in range(self.size)]):
                return True
        # Vérifications diagonales
        for d in range(-self.size + 1, self.size):
            if self.check_line_win([self.board[i][i + d] for i in range(max(0, -d), min(self.size, self.size - d))]):
                return True
            if self.check_line_win([self.board[i][self.size - 1 - i + d] for i in range(max(0, d), min(self.size, self.size + d))]):
                return True
        return False

    def check_line_win(self, line):
        # Vérifie si une ligne contient un nombre suffisant de symboles consécutifs pour gagner
        consecutive_count = 0
        last_symbol = ' '
        for symbol in line:
            if symbol == last_symbol and symbol != ' ':
                consecutive_count += 1
            else:
                consecutive_count = 1
                last_symbol = symbol
            if consecutive_count >= self.win_length:
                return True
        return False

    def is_game_over(self):
        if self.check_win():  # Si un joueur a gagné
            return True
        for row in self.board:
            if ' ' in row:  # S'il reste des mouvements valides
                return False
        return True  # Le plateau est plein, donc le jeu est terminé

    def get_all_lines(self):
        # Cette méthode devrait renvoyer toutes les lignes, colonnes et diagonales pour l'évaluation
        lines = []
        # Ajouter les lignes horizontales et verticales
        for i in range(self.size):
            lines.append(self.board[i])  # lignes horizontales
            lines.append([self.board[j][i]
                         for j in range(self.size)])  # lignes verticales

        # Ajouter les diagonales
        diagonals = [[self.board[i][i] for i in range(self.size)], [
            self.board[i][self.size-1-i] for i in range(self.size)]]
        lines.extend(diagonals)
        return lines
