from game_logic import Game
from minimax_algorithm import \
    find_best_move  # Assurez-vous que cette fonction est correctement définie.


def main():
    game = Game()
    while True:
        game.print_board()
        if game.current_player == 'X':
            row, col = map(int, input(
                "Enter row and column numbers to make a move (e.g., '1 2'): ").split())
        else:
            print("Computer's turn:")
            move = find_best_move(game)
            if move is not None:
                row, col = move
            else:
                print("No valid moves left. Game Over.")
                break

        if game.make_move(row, col):
            if game.check_win():
                game.print_board()
                print(f"Player {game.current_player} wins!")
                break
            game.switch_player()
        else:
            print("Invalid move. Try again.")

        if all(game.board[row][col] != ' ' for row in range(game.size) for col in range(game.size)):
            print("The game is a tie!")
            break


if __name__ == "__main__":
    main()
