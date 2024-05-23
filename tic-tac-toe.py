import random


def display_board(board):
    """
    Выводит текущее состояние доски.
    """
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):
    """
    Проверяет, есть ли победитель.
    """
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def get_computer_move(board):
    """
    Возвращает случайный ход компьютера.
    """
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(available_moves)


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    values = ['X', '0']
    player = values[0]

    random.shuffle(values)
    user = values[0]
    computer = values[1]

    print("Добро пожаловать в игру Крестики-Нолики!")
    print("Игровое поле имеет следующий формат:")
    print("1|2|3\n4|5|6\n7|8|9\n")

    while True:
        display_board(board)
        if player == user:
            move = input("Выберите позицию для вашего хода (1-9): ")
            try:
                move = int(move) - 1
                row = move // 3
                col = move % 3

                if move < 0 or move > 8 or board[row][col] != " ":
                    print("Некорректный ход. Попробуйте снова.")
                    continue

                board[row][col] = player

                if check_winner(board, player):
                    display_board(board)
                    print(f"Игрок ({player}) победил!")
                    break

                player = computer

            except ValueError:
                print("Введите число от 1 до 9.")
        else:
            row, col = get_computer_move(board)
            board[row][col] = computer
            print(f"Компьютер выбрал позицию {row * 3 + col + 1}")

            if check_winner(board, computer):
                display_board(board)
                print(f"Компьютер ({computer}) победил!")
                break

            player = user

        if all(cell != " " for row in board for cell in row):
            display_board(board)
            print("Ничья!")
            break


if __name__ == "__main__":
    main()
