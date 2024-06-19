a = int(input("enter value for first number : "))
b = int(input("enter value second number : "))
c = int(input("enter the third number : "))
d = int(input("enter the fourth number: "))

if a<b and a<c and a<d:
    print(a,"is the smallest number")
if b < a and b < c and b < d:
    print(b, "is the smallest number")
if c<a and c<b and c<d:
    print(c,"is the smallest number")
if d < a and d < b and d < c:
    print(d, "is the smallest number")

