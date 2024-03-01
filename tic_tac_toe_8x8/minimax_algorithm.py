def minimax_with_dls(board, max_depth, depth, alpha, beta, is_maximizing_player):
    if board.is_game_over() or depth == 0:
        return evaluate_board(board)

    if is_maximizing_player:
        max_eval = float('-inf')
        for move in board.get_valid_moves():
            row, col = move
            board.make_move(row, col)
            eval = minimax_with_dls(
                board, max_depth, depth - 1, alpha, beta, False)
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
            eval = minimax_with_dls(
                board, max_depth, depth - 1, alpha, beta, True)
            board.undo_move(row, col)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def find_best_move(board, max_depth=2):
    best_eval = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    for move in board.get_valid_moves():
        row, col = move
        board.make_move(row, col)
        eval = minimax_with_dls(
            board, max_depth, max_depth, alpha, beta, False)
        board.undo_move(row, col)
        if eval > best_eval:
            best_eval = eval
            best_move = move
        alpha = max(alpha, eval)
    return best_move


def evaluate_board(board):

    WIN_SCORE = 100
    LOSE_SCORE = -100

    if board.is_winner('O'):
        return WIN_SCORE
    elif board.is_winner('X'):
        return LOSE_SCORE
    else:
        return 0
