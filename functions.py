# inbuilt functions
# standard library functions
y = min(23, 56, 1000, 5647)
print(y)

x = max(65, 2, 66, 98)
print("the maximum number is", x)

#returning the power of a value
z = pow(6 , 3)
print(z)

# user defined functions
def school():
    print("eMobilis")
school() #calling a function

def multiply():
    num1 = 7
    num2 = 8
    print(num1*num2)
multiply()
#parameters and arguments
def add(a, b):
    print(a+b)
add(7, 90)
add(8, 79)
add(12, 4)
add(18, 2)

#printing multiple details
def Employee(fullname,age,salary,phone,position):
    print(fullname,age,salary,phone,position)

Employee("Job kamau", 21, 46000, 712345678, "MD")
Employee("Maina kamau", 27, 40000, 700046578, "sec")
Employee("Grace Kwamboka", 23, 50000, 732146578, "IT")
Employee("wambui Anne", 22, 36000, 789046578, "Receptionist")


