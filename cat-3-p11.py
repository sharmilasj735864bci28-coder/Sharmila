# 1. Define your list first to avoid the 'not defined' error
L = [2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 8, 10, 3]

# 2. Use a dictionary to count occurrences
counts = {}
for num in L:
    counts[num] = counts.get(num, 0) + 1

# 3. Print numbers that appear exactly twice
for num in counts:
    if counts[num] == 2:
        print(num)
