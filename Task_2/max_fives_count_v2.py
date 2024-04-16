def max_fives_count_in_sequence(n, marks):
    max_fives_count = 0
    current_fives_count = 0
    current_sequence = 0
    found_sequence = False

    for i in range(n):
        if marks[i] == 5 and current_sequence < 7:
            current_fives_count += 1
        if marks[i] != 2 and marks[i] != 3:
            current_sequence += 1
            if current_sequence == 7 or (len(marks) // 2) < 7:  # 5 5 5 5 5 3 5 5 5 5 5 5 5 5 5 5 5 5 5 5
                found_sequence = True
        else:
            if found_sequence:
                max_fives_count = max(max_fives_count, current_fives_count)
                found_sequence = False
            current_fives_count = 0
            current_sequence = 0

    if found_sequence:
        max_fives_count = max(max_fives_count, current_fives_count)

    if max_fives_count == 0:
        return -1
    else:
        return max_fives_count


n = int(input())
marks = list(map(int, input().split()))

print(max_fives_count_in_sequence(n, marks))
### последний отправленный вариант