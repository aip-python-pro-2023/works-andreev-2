# Базовый (родительский) класс
class Recipe:
    def __init__(self, name, ingredients):
        self._name = name
        self._ingredients = ingredients

    def get_dishes(self):
        pass

    # Реализация оператора in
    # sugar in recipe
    def __contains__(self, item):
        return item in self._ingredients

    def __str__(self):
        return f'Recipe(name={self._name})'


# Дочерний класс 1
class DrinkRecipe(Recipe):
    def __init__(self, name, ingredients, volume):
        super().__init__(name, ingredients)
        self._volume = volume

    def __str__(self):
        return f'DrinkRecipe(name={self._name}, volume={self._volume})'

    def get_dishes(self):
        return ['стакан', 'чашка', 'бокал']


class FoodRecipe(Recipe):
    def __init__(self, name, ingredients, serving):
        super().__init__(name, ingredients)
        self._serving = serving

    def __str__(self):
        return f'FoodRecipe(name={self._name}, serving={self._serving})'

    def get_dishes(self):
        return ['тарелка', 'нож', 'вилка']


latte = DrinkRecipe('Латте', ['кофейные зёрна', 'молоко', 'ванильный сироп'], 0.5)
lasagna = FoodRecipe('Лазанья', ['Фарш', 'Соус бешамель', 'Листы для лазаньи', 'Сыр', 'Соус болоньезе'], 4)

print(latte)
print(lasagna)

print(latte.get_dishes())
print(lasagna.get_dishes())
