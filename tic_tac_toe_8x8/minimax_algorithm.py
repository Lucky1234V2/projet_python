def minimax(board, depth, alpha, beta, is_maximizing_player):
    if board.is_game_over() or depth == 0:
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
                break  # Élagage alpha-bêta
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
                break  # Élagage alpha-bêta
        return min_eval


def find_best_move(board, depth=6):
    best_eval = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    valid_moves = board.get_valid_moves()
    # Trie les mouvements en fonction de leur évaluation potentielle
    sorted_moves = sorted(
        valid_moves, key=lambda move: evaluate_move(board, move), reverse=True)
    for move in sorted_moves:
        row, col = move
        board.make_move(row, col)
        eval = minimax(board, depth - 1, alpha, beta, False)
        board.undo_move(row, col)
        if eval > best_eval:
            best_eval = eval
            best_move = move
        alpha = max(alpha, eval)
    return best_move

# Une fonction pour évaluer le potentiel d'un mouvement


def evaluate_move(board, move):
    row, col = move
    board.make_move(row, col)
    score = evaluate_board(board)
    board.undo_move(row, col)
    return score

# La fonction d'évaluation de la position du plateau


def evaluate_board(board):
    score = 0
    lines_to_check = board.get_all_lines()
    for line in lines_to_check:
        x_count = line.count('X')
        o_count = line.count('O')
        if x_count >= board.win_length - 1:  # Détecter les menaces de l'adversaire
            score -= 100
        if o_count >= board.win_length - 1:  # Rechercher les opportunités de gagner
            score += 100
        # Détecter les opportunités de former une ligne gagnante
        if x_count == board.win_length - 2 and ' ' in line:
            score -= 50
        if o_count == board.win_length - 2 and ' ' in line:  # Détecter les menaces de l'adversaire
            score += 50
    return score
