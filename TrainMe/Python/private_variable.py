class Cup:
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = None  # private variable

    def fill(self, beverage):
        self.__content = beverage

    def empty(self):
        self.__content = None

# Instance of class Cup
redCup = Cup("red")
redCup._Cup__content = "tea"
print redCup
