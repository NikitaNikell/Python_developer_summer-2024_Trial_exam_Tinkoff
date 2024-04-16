def rotate_matrix(matrix, direction):
    n = len(matrix)
    operations = []
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            x1, y1 = i, j
            x2, y2 = j, n - i - 1
            x3, y3 = n - i - 1, n - j - 1
            x4, y4 = n - j - 1, i

            if direction == "R":
                operations.append((x1, y1, x2, y2))
                operations.append((x1, y1, x3, y3))
                operations.append((x1, y1, x4, y4))
            elif direction == "L":
                operations.append((x1, y1, x4, y4))
                operations.append((x1, y1, x3, y3))
                operations.append((x1, y1, x2, y2))

    max_operations = min(7 * n * n, len(operations))  # Учитываем ограничение на количество операций
    return operations[:max_operations]

n, direction = input().split()  # Считываем размер матрицы и направление поворота
n = int(n)

matrix = [list(map(int, input().split())) for _ in range(n)]  # Считываем матрицу

operations = rotate_matrix(matrix, direction)  # Получаем последовательность операций для поворота

print(len(operations))  # Выводим количество операций

for operation in operations:  # Выводим каждую операцию
    print(*operation)
