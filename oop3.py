class device:
    def __init__(self,model,yom):
        self.model = model
        self.yom = yom
    def crush(self):
        print(self.model, "has crushed")

computer = device("HP","2010")

laptop = device("asus","2015")
