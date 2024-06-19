try:
    print(x)

except:
    print("an error occurred")

finally:
    print("success")

num1 = 45
num2 = 0
try:
    print(num1 / num2)
except:
    print("zeroDivision error occurred")
finally:
    print("success")