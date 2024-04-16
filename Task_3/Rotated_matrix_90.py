n, m = map(int, input().split())    # Размеры матрицы.

original_matrix = [list(map(int, input().split())) for _ in range(n)]    # Получаем исходную матрицу
#rotated_matrix = [[original_matrix[n - j - 1][i] for j in range(n)] for i in range(m)]    # Поворот матрицы на 90 гр.

for i in range(m):
    for j in range(n - 1, -1, -1):
        print(original_matrix[j][i], end=' ')
    print()

#for row in rotated_matrix:
#    print(*row)

# TEST:

