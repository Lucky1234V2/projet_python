def minimax(board, depth, alpha, beta, is_maximizing_player):
    if board.is_game_over() or depth == 0:
        # Assurez-vous que evaluate_board retourne toujours une valeur numérique.
        return evaluate_board(board)

    if is_maximizing_player:
        max_eval = float('-inf')
        for move in board.get_valid_moves():
            row, col = move
            board.make_move(row, col)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.undo_move(row, col)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.get_valid_moves():
            row, col = move
            board.make_move(row, col)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.undo_move(row, col)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def find_best_move(board, depth=6):
    best_eval = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    for move in board.get_valid_moves():
        row, col = move
        board.make_move(row, col)
        eval = minimax(board, depth - 1, alpha, beta, False)
        board.undo_move(row, col)
        if eval > best_eval:
            best_eval = eval
            best_move = move
        alpha = max(alpha, eval)
    return best_move


def evaluate_board(board):
    # Hypothèse: board est une matrice 8x8 et board[x][y] retourne l'état de la case (par ex., vide, 'X', ou 'O')

    # Constantes pour les scores
    WIN_SCORE = 100
    LOSE_SCORE = -100

    # Vérifie si le jeu est terminé et qui a gagné pour attribuer un score simple
    if board.is_winner('O'):  # Adaptez cette condition à votre implémentation
        return WIN_SCORE
    elif board.is_winner('X'):  # Adaptez cette condition à votre implémentation
        return LOSE_SCORE
    else:
        # Pour une évaluation plus sophistiquée, considérez le nombre de séquences partielles (par ex., deux ou trois en ligne)
        # et ajustez les scores en conséquence. Cela peut nécessiter une logique plus complexe.
        return 0  # Retourne un score neutre si le jeu n'est pas encore décidé
