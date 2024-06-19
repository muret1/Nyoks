# CLASS IA A BLUEPRINT OF OBJECT
# OBJECT IS AN INSTANCE OF  A CLASS

class person:
    # characteristics
    name = "James"
    age = 32
    gender = "male"

    # functions
    def move(self):
        print("person is walking")

farmer = person()
farmer.move()
print(farmer.gender)

