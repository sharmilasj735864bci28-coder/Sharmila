counts = {}
for num in L:
    counts[num] = counts.get(num, 0) + 1
for num in counts:
    if counts[num] == 2:
        print(num)


    
