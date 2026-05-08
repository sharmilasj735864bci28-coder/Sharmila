def add_numbers(x,y):
    sum=x+y
    return sum
result=add_numbers(3,6)
print(result)



sum=lambda x,y:x+y
print ("sum",sum(3,5))




simple_interest = lambda p, r, t: (p * r * t) / 100

print("Simple Interest:", simple_interest(1000, 5, 2))



def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = check_even_odd(7)
print("The number 7 is:", result) 
