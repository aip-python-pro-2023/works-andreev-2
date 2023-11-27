class Ingredient:
    # Поле - переменная в классе
    # Метод - функция в классе

    # Конструктор, вызывается при создании объекта класса Ingredient
    def __init__(self, ingredient_id, name, description, ingredient_type, picture, calories, proteins, fats, carbohydrates):
        self.id = ingredient_id
        self.name = name
        self.description = description
        self.type = ingredient_type
        self.picture = picture
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    # Деструктор, вызывается при удалении объекта, обычно не нужен
    def __del__(self):
        print('Deleting :\'(')

    def add_description(self, desc):
        self.description = desc


carrot = Ingredient(1, 'Морковь', 'Вкусный и полезный овощ', 'Овощ', 'https://vkustorg.com/image/cache/Ovochi_frukty/1460024087-500x500.jpg', 150, 70, 10, 20)
print(carrot.name)
print(carrot.description)

del carrot

sugar = Ingredient(2, 'Сахар', 'Сладкая вещь, с которой не стоит перебарщивать', 'Бакалея', 'https://centrstomatologii.ru/upload/resize_cache/webp/iblock/8b9/fe1rhhjon2lrtjfaqjoejc14elz4xk8s/1300_850_1/wide_4_3_821a7b2af4c4914631b84d86a6cafaad.webp', 250, 0, 0, 100)
print(sugar.name)
print(sugar.description)
