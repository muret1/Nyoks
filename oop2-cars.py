class car:
      def __init__(self,model,color,manufacturer,year):
          self.model = model
          self.color = color
          self.manufacturer = manufacturer
          self.year = year


      def speed(self):
          print("The manufacturer of", self.model, "is", self.manufacturer)

car1 = car("m-5", "black", "BMW", 2002)
car2 = car("m-5", "black", "BMW", 2002)
car3 = car("m-5", "black", "BMW", 2002)
car4 = car("m-5", "black", "BMW", 2002)
