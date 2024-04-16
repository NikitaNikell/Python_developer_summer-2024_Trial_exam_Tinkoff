from collections import deque


# Функция для проверки допустимости хода
def is_valid_move(x, y, n):
    return 0 <= x < n and 0 <= y < n


# Функция для определения минимального количества ходов
def min_moves(n, board):
    # Начальные координаты старта и финиша
    start = finish = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'S':
                start = (i, j)
            elif board[i][j] == 'F':
                finish = (i, j)

    # Очередь для BFS
    queue = deque([(start, 0, 'K')])
    visited = set()
    visited.add((start, 'K'))

    # Возможные направления хода коня
    knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    # Возможные направления хода короля
    king_moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    # BFS для поиска минимального количества ходов
    while queue:
        (x, y), moves, piece = queue.popleft()

        # Если достигли финиша, возвращаем количество ходов
        if (x, y) == finish:
            return moves

        # Выбираем возможные направления хода в зависимости от типа фигуры
        if piece == 'K':
            moveset = knight_moves
        else:
            moveset = king_moves

        # Проверяем все возможные направления хода
        for dx, dy in moveset:
            new_x, new_y = x + dx, y + dy

            # Если новые координаты допустимы и не посещались ранее
            if is_valid_move(new_x, new_y, n) and (new_x, new_y, piece) not in visited:
                # Если на новой клетке фишка
                if board[new_x][new_y] != '.':
                    # Если фишка K, меняем тип фигуры на коня
                    if board[new_x][new_y] == 'K':
                        queue.append(((new_x, new_y), moves + 1, 'K'))
                    # Если фишка G, меняем тип фигуры на короля
                    elif board[new_x][new_y] == 'G':
                        queue.append(((new_x, new_y), moves + 1, 'Q'))
                # Иначе добавляем новую клетку в очередь для дальнейшего поиска
                else:
                    queue.append(((new_x, new_y), moves + 1, piece))
                visited.add((new_x, new_y, piece))

    # Если финиш не достижим
    return -1


# Считываем входные данные
n = int(input())
board = [input() for _ in range(n)]

# Вызываем функцию и выводим результат
print(min_moves(n, board))




