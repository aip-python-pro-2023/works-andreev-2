class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    # Реализация оператора in
    # sugar in recipe
    def __contains__(self, item):
        return item in self.ingredients
