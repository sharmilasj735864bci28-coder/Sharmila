n=5
for i in range (n):
    for j in range(i+1):
        print('*',end=" ")
    print()

n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
        print()

n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
print()



n=5
for i in range (n):
    for j in range(i+1):
        print('*',end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print('*',end=" ")
    print()
    

def pattern3(n):
    for i in range(1, n + 1):
       for j in range(n - i):
            print(" ", end="")
       for k in range(i):
            print(chr(65 + k), end=" ")
       print()  
pattern3(5)
