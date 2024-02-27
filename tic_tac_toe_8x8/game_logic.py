class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.current_player = 'X'  # Ajoutez cette ligne pour initialiser le joueur courant
        self.size = 8

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

    def print_board(self):
        # Affiche l'état actuel du plateau de jeu
        print('  ' + ' '.join(str(i) for i in range(self.size)))
        print('+---' * self.size + '+')
        for row in range(self.size):
            print('| ' + ' | '.join(self.board[row]) + ' |')
            print('+---' * self.size + '+')

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
        # Optimisation : Privilégier les cases proches des jetons déjà placés pour réduire l'espace de recherche
        moves = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == ' ':
                    if any(self.board[r][c] != ' ' for r, c in self.get_neighbors(row, col)):
                        moves.append((row, col))
        return moves

    def get_neighbors(self, row, col):
        # Renvoie les cases adjacentes (8 directions possibles)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            if 0 <= row + dr < self.size and 0 <= col + dc < self.size:
                yield row + dr, col + dc

    def is_game_over(self):
        # Vérifie si le jeu est terminé
        return self.check_win('X') or self.check_win('O') or all(self.board[row][col] != ' ' for row in range(self.size) for col in range(self.size))

    def check_win(self, player):
        # Vérifie si le joueur a gagné
        for row in range(self.size):
            for col in range(self.size):
                if any(self.check_line(row, col, dr, dc, player) for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]):
                    return True
        return False

    def check_line(self, row, col, dr, dc, player):
        # Vérifie une ligne de 4 jetons du même joueur
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
