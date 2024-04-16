def max_mushrooms(n, forest):
    dp = [[0] * len(forest[0]) for _ in range(n)]

    for j in range(len(forest[0])):
        if forest[n - 1][j] == 'C':
            dp[n - 1][j] = 1

    for i in range(n - 2, -1, -1):
        for j in range(len(forest[i])):
            if forest[i][j] == 'W':
                continue
            for dj in range(-1, 2):
                if 0 <= j + dj < len(forest[i + 1]):
                    dp[i][j] = max(dp[i][j], dp[i + 1][j + dj] + (forest[i][j] == 'C'))

    max_mushrooms_count = max(dp[0])

    return max_mushrooms_count


n = int(input())

forest = [list(input()) for _ in range(n)]

print(max_mushrooms(n, forest))

# Пример использования:
# n = 5
# forest = [
#     "W.W",
#     "C.C",
#     "WW.",
#     "CC.",
#     "CWW"
#     ]


# n = 4
# forest = [
#     'W.W',
#     'CWC',
#     'W.W',
#     'CWW'
# ]

# n = 4
#
# forest = [
#     'W.W',
#     '..C',
#     'WW.',
#     'C..'
# ]
