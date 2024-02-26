from game_logic import TicTacToe
from minimax_algorithm import find_best_move


def main():
    game = TicTacToe()
    while not game.is_game_over():
        game.print_board()
        if game.current_player == 'X':
            row, col = map(int, input(
                "Enter row and column numbers to make a move (e.g., '1 2'): ").split())
            if not game.make_move(row, col):
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's turn:")
            move = find_best_move(game)
            if move:
                row, col = move
                game.make_move(row, col)
            else:
                print("No valid moves left. Game Over.")
                break

        if game.check_win(game.current_player):
            game.print_board()
            print(f"Player {game.current_player} wins!")
            break
        elif all(game.board[row][col] != ' ' for row in range(game.size) for col in range(game.size)):
            print("The game is a tie!")
            break

        # Switch player is handled inside make_move, so it's no longer needed here
        # game.switch_player() # This function doesn't exist in the provided code and isn't needed


if __name__ == "__main__":
    main()
