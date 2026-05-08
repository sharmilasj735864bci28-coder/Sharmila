user_input = input("Enter 10 integers separated by space: ")
nums = list(map(int, user_input.split()))
MyList1 = []
MyList2 = []
for x in nums:
    if x % 2 != 0 and x % 3 != 0:
        MyList1.append(x)
    if x % 9 == 0:
        MyList2.append(x)
print(*(MyList1))
print(*(MyList2))

out put:
Enter 10 integers separated by space: 1 5 7 9 11 17 19 27 45 50
1 5 7 11 17 19
9 27 45
