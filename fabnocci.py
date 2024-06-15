n=int(input("enter the number of terms:"))
a=0
b=1
c=a+b
print("fibnocci series",a,b)
for i in range(2,n):
    a=b
    b=c
    c=a+b
    print(c)
print()