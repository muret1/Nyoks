num2 = int(input("Enter first number :"))
num1 = int(input("Enter second number :"))


working = input("Enter working:"
                "- for subtraction"
                "+ for addition"
                "/ for division"
                "* for multiplication")

if working == "+":
    print("Result", num1+num2)
elif working == "-":
    print("Result", num1 - num2)
elif working == "*":
    print("Result", num1 * num2)
elif working == "/":
    print("Result", num1 / num2)
if num1 == 0:
    print("error!")
else:
    print("result:", num1/num2)
    print("input invalid")




