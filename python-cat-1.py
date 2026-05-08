# 1. Read the number of elements (n)
n = int(input())

# 2. Read the line of space-separated integers and convert them to a list
data = list(map(int, input().split()))

# 3. Apply logic: x**2 if even, x**3 if odd
result = [x**2 if x % 2 == 0 else x**3 for x in data]

# 4. Convert the final list to a tuple and print
print(tuple(result))
