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
    TWO_IN_ROW_SCORE = 10
    TWO_IN_ROW_OPPONENT_SCORE = -20

    if board.is_winner('O'):
        return WIN_SCORE
    elif board.is_winner('X'):
        return LOSE_SCORE
    else:
        score = 0
        # Parcourir le plateau pour évaluer les alignements de deux symboles
        for row in range(board.size):
            for col in range(board.size):
                # Évaluer les alignements horizontaux, verticaux et diagonaux
                if board.board[row][col] == ' ':
                    # Vérifier les alignements horizontaux et verticaux
                    if col <= 5 and board.board[row][col + 1] == board.board[row][col + 2] != ' ':
                        score += TWO_IN_ROW_SCORE if board.board[row][col +
                                                                      1] == 'O' else TWO_IN_ROW_OPPONENT_SCORE
                    if row <= 5 and board.board[row + 1][col] == board.board[row + 2][col] != ' ':
                        score += TWO_IN_ROW_SCORE if board.board[row +
                                                                 1][col] == 'O' else TWO_IN_ROW_OPPONENT_SCORE

                    # Vérifier les alignements diagonaux
                    if row <= 5 and col <= 5 and board.board[row + 1][col + 1] == board.board[row + 2][col + 2] != ' ':
                        score += TWO_IN_ROW_SCORE if board.board[row +
                                                                 1][col + 1] == 'O' else TWO_IN_ROW_OPPONENT_SCORE
                    if row >= 2 and col <= 5 and board.board[row - 1][col + 1] == board.board[row - 2][col + 2] != ' ':
                        score += TWO_IN_ROW_SCORE if board.board[row -
                                                                 1][col + 1] == 'O' else TWO_IN_ROW_OPPONENT_SCORE

        return score
