from .item import Item


class Clothing(Item):
    def __init__(self, condition = None, age = None):
        category = "Clothing"
        super().__init__(category, condition, age)



    
    def __str__(self):
        return "The finest clothing you could wear."