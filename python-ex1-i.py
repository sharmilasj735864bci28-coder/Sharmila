s1=int(input("Enter a mark1:"))
s2=int(input("Enter a mark2:"))
s3=int(input("Enter a mark3:"))
s4=int(input("Enter a mark4:"))
total=s1+s2+s3+s4
agg=(total/4)
print(total)
print(agg)
if(agg>75):
    print("Distinction")
elif(60<=agg>75):
    print("First divition")
elif(50<=agg>60):
    print("Second divition")
elif(40<=agg>50):
    print("Third divition")
else:
    print("Fail")
