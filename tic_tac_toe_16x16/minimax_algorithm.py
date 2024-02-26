def find_best_move(game):
    best_score = float('-inf')
    best_move = None
    for row in range(game.size):
        for col in range(game.size):
            if game.is_valid_move(row, col):
                game.make_move(row, col)
                score = minimax(game, 0, False, float('-inf'), float('inf'))
                game.undo_move(row, col)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


def minimax(game, depth, is_maximizing, alpha, beta):
    if game.check_win():
        return 1000 if is_maximizing else -1000
    if depth == 0:
        return evaluate_board(game)

    if is_maximizing:
        max_eval = float('-inf')
        for row in range(game.size):
            for col in range(game.size):
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
        for row in range(game.size):
            for col in range(game.size):
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


def evaluate_board(game):
    score = 0
    # Exemple : +10 pour chaque séquence de 3 'X' ou 'O' sans blocage, -10 pour l'adversaire
    # Vous pouvez développer cela avec des scores pour différentes configurations
    for row in range(game.size):
        for col in range(game.size):
            if game.board[row][col] == game.current_player:
                score += 10  # ou une autre logique basée sur la configuration autour de cette pièce
            elif game.board[row][col] != ' ':
                score -= 10  # ajuster pour l'opposant
    return score
