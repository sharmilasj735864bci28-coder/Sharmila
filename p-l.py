n1, n2 = map(int, input().split())
for current_end in range(n2, n1 - 1, -1):
    for i in range(n1, current_end + 1):
        print(i, end=" ")
    print()
