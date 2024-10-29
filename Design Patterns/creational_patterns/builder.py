class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = None
    
    def setBun(self, bunStyle):
        self.bun = bunStyle
    
    def setPatty(self, pattyStyle):
        self.patty = pattyStyle
    
    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle

    def print(self):
        print(self.bun, self.patty, self.cheese)
    

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def addBun(self, bunStyle):
        self.burger.setBun(bunStyle)
        return self

    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    def build(self):
        return self.burger
    
if __name__ == "__main__":
    burgerBuilder = BurgerBuilder()
    burger = BurgerBuilder().addBun("bun").addPatty("beef").addCheese("cheddar").build()
    burger.print()

# Source: NeetCode