import recipe


class Ingredient:
    # Поле - переменная в классе
    # Метод - функция в классе

    # Статическое поле - поле, которое относится к классу в целом, а не к какому-то объекту
    current_id = 1

    # Конструктор, вызывается при создании объекта класса Ingredient
    def __init__(self, name, description, ingredient_type, picture, calories, proteins, fats, carbohydrates):
        self.id = Ingredient.current_id
        Ingredient.current_id += 1
        self.name = name
        self.description = description
        self.type = ingredient_type
        self.picture = picture
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    # Превращаем объект в строчку
    def __str__(self):
        return f'Ingredient(id={self.id}, name={self.name}, calories={self.calories}, proteins={self.proteins}, fats={self.fats}, carbohydrates={self.carbohydrates})'

    # Проверка на равенство
    def __eq__(self, other):
        return isinstance(other, Ingredient) and self.name == other.name

    @staticmethod
    def create_from_input():
        return Ingredient(
            name=input('Введите имя ингредиента: '),
            description=input('Введите описание: '),
            ingredient_type=input('Выберите тип: '),
            picture=input('Добавьте ссылку на изображение: '),
            calories=float(input('Калории (на 100 г.): ')),
            proteins=float(input('Белки (на 100 г.): ')),
            fats=float(input('Жиры (на 100 г.): ')),
            carbohydrates=float(input('Углеводы (на 100 г.): ')),
        )


carrot = Ingredient('Морковь', 'Вкусный и полезный овощ', 'Овощ', 'https://vkustorg.com/image/cache/Ovochi_frukty/1460024087-500x500.jpg', 150, 70, 10, 20)
print(carrot)
print(carrot.name)
print(carrot.description)

sugar = Ingredient('Сахар', 'Сладкая вещь, с которой не стоит перебарщивать', 'Бакалея', 'https://centrstomatologii.ru/upload/resize_cache/webp/iblock/8b9/fe1rhhjon2lrtjfaqjoejc14elz4xk8s/1300_850_1/wide_4_3_821a7b2af4c4914631b84d86a6cafaad.webp', 250, 0, 0, 100)
print(sugar)
print(sugar.name)
print(sugar.description)

# Не делайте так
# print(Ingredient.current_id)
# sugar.current_id += 1
# print(Ingredient.current_id)
# print(sugar.current_id)

nice_recipe = recipe.Recipe('Вкусный пирог', [sugar, carrot])

print(sugar == carrot)
print(sugar == nice_recipe)

print('Sugar in nice recipe:', sugar in nice_recipe)

bread = Ingredient.create_from_input()
print(bread)
