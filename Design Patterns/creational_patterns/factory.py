class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def print(self):
        print(self.ingredients)

class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)
    def createDeluxeBurger(self):
        ingredients = ["bun", "cheese", "beef-patty", "lettuce", "tomato", "onions"]
        return Burger(ingredients)
    
if __name__ == "__main__":
    burgerFactory = BurgerFactory()
    burgerFactory.createCheeseBurger().print()
    burgerFactory.createDeluxeBurger().print()

# Source: NeetCode