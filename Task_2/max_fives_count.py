
def max_fives_count_in_sequence(marks):
    max_fives_count = 0
    current_fives_count = 0
    current_sequence = 0
    found_sequence = False

    for mark in marks:
        if mark == 5 and current_sequence < 7:
            current_fives_count += 1
        if mark not in [2, 3]:
            current_sequence += 1
            if current_sequence == 7:
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


#n = int(input())
#marks = list(map(int, input().split()))

#print(max_fives_count_in_sequence(marks))


#TEST:
marks1 = [5, 5, 4, 5, 4, 5, 4, 5, 4]
marks2 = [3, 4, 4, 4, 4, 5, 4, 5]
marks3 = [5, 5, 5, 5, 5, 3, 5, 5, 5, 5]

assert max_fives_count_in_sequence(marks1) == 4, "Error test:1"
assert max_fives_count_in_sequence(marks2) == 2, "Error test: 3"
assert max_fives_count_in_sequence(marks3) == -1, "Error test:3"

print('GOOD')

