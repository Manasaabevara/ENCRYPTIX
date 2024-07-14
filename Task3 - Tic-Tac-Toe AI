import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.full((3, 3), ' ')
        self.current_player = 'X'  # Human starts first

    def print_board(self):
        print("\n".join([' | '.join(row) for row in self.board]))
        print()

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i, j] == player for j in range(3)) or \
               all(self.board[j, i] == player for j in range(3)):
                return True
        if all(self.board[i, i] == player for i in range(3)) or \
           all(self.board[i, 2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return np.all(self.board != ' ')

    def minimax(self, depth, is_maximizing):
        if self.is_winner('O'):
            return 1  # AI wins
        elif self.is_winner('X'):
            return -1  # Human wins
        elif self.is_draw():
            return 0  # Draw

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i, j] == ' ':
                        self.board[i, j] = 'O'
                        score = self.minimax(depth + 1, False)
                        self.board[i, j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i, j] == ' ':
                        self.board[i, j] = 'X'
                        score = self.minimax(depth + 1, True)
                        self.board[i, j] = ' '
                        best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = float('-inf')
        move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i, j] == ' ':
                    self.board[i, j] = 'O'
                    score = self.minimax(0, False)
                    self.board[i, j] = ' '
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def play(self):
        while True:
            self.print_board()
            if self.current_player == 'X':
                try:
                    row, col = map(int, input("Enter row and column (0-2) for X (separated by a space): ").split())
                    if self.board[row, col] != ' ':
                        print("Invalid move! The cell is already taken. Try again.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter two numbers separated by a space.")
                    continue
                except IndexError:
                    print("Invalid input! Please enter numbers between 0 and 2.")
                    continue
            else:
                row, col = self.best_move()

            self.board[row, col] = self.current_player

            if self.is_winner(self.current_player):
                self.print_board()
                print(f"{self.current_player} wins!")
                break
            elif self.is_draw():
                self.print_board()
                print("It's a draw!")
                break

            self.current_player = 'X' if self.current_player == 'O' else 'O'

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
