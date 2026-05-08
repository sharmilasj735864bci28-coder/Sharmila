# Accept two integers N1 and N2 as input
n1, n2 = map(int, input().split())

# Outer loop determines the ending number for each row
# It starts at n2 and decreases down to n1
for current_end in range(n2, n1 - 1, -1):
    
    # Inner loop prints numbers from n1 up to the current_end
    for i in range(n1, current_end + 1):
        print(i, end=" ")
    
    # Print a newline to start the next row
    print()
