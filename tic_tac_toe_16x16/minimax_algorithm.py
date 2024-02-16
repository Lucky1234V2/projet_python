def find_best_move(game):
    best_score = float('-inf')
    best_move = None
    for row in range(16):
        for col in range(16):
            if game.is_valid_move(row, col):
                game.make_move(row, col)
                score = minimax(game, 0, False, float('-inf'), float('inf'))
                game.undo_move(row, col)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


def minimax(game, depth, is_maximizing, alpha, beta):
    if depth == 0 or game.check_win_condition():
        return game.evaluate_board()

    if is_maximizing:
        max_eval = float('-inf')
        for row in range(16):
            for col in range(16):
                if game.is_valid_move(row, col):
                    game.make_move(row, col)
                    evaluation = minimax(game, depth - 1, False, alpha, beta)
                    game.undo_move(row, col)
                    max_eval = max(max_eval, evaluation)
                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(16):
            for col in range(16):
                if game.is_valid_move(row, col):
                    game.make_move(row, col)
                    evaluation = minimax(game, depth - 1, True, alpha, beta)
                    game.undo_move(row, col)
                    min_eval = min(min_eval, evaluation)
                    beta = min(beta, evaluation)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return min_eval


def check_win(self, row, col):
    player = self.board[row][col]
    # Horizontal, vertical, deux diagonales
    for direction in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        count = 1
        for d in [1, -1]:  # Deux directions pour chaque ligne/colonne/diagonale
            for step in range(1, 5):  # Vérifier jusqu'à 4 pions de chaque côté
                r, c = row + step * direction[0] * \
                    d, col + step * direction[1] * d
                if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == player:
                    count += 1
                else:
                    break
            if count >= 5:  # Vous pouvez ajuster ce nombre selon les règles de votre jeu
                return True
    return False


def undo_move(self, row, col):
    self.board[row][col] = ' '
