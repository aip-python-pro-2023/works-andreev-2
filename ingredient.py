import recipe


class Ingredient:
    # Поле - переменная в классе
    # Метод - функция в классе

    # Статическое поле - поле, которое относится к классу в целом, а не к какому-то объекту
    current_id = 1

    # Конструктор, вызывается при создании объекта класса Ingredient
    def __init__(self, name, description, ingredient_type, picture, calories, proteins, fats, carbohydrates):
        self.__id = Ingredient.current_id
        Ingredient.current_id += 1
        self.__name = name
        self.__description = description
        self.__type = ingredient_type
        self.__picture = picture
        self.__calories = calories
        self.__proteins = proteins
        self.__fats = fats
        self.__carbohydrates = carbohydrates

    # Геттер
    def get_fats(self):
        return self.__fats

    # Сеттер
    def set_fats(self, new_fats):
        if 0 <= new_fats <= 100:
            self.__fats = new_fats

    @property
    def fats(self):
        return self.__fats

    @fats.setter
    def fats(self, value):
        print('Property setter')
        if 0 <= value <= 100:
            self.__fats = value

    # Превращаем объект в строчку
    def __str__(self):
        return f'Ingredient(id={self.__id}, name={self.__name}, calories={self.__calories}, proteins={self.__proteins}, fats={self.__fats}, carbohydrates={self.__carbohydrates})'

    # Проверка на равенство
    def __eq__(self, other):
        return isinstance(other, Ingredient) and self.__name == other.__name

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
# carrot.__fats = 5000
print(carrot)
print(carrot.get_fats())
carrot.set_fats(0)
print(carrot)

# carrot.__fats += 10

# Через геттер и сеттер
carrot.set_fats(carrot.get_fats() + 120)
# Через свойства
carrot.fats += 120
print(carrot.fats)

sugar = Ingredient('Сахар', 'Сладкая вещь, с которой не стоит перебарщивать', 'Бакалея', 'https://centrstomatologii.ru/upload/resize_cache/webp/iblock/8b9/fe1rhhjon2lrtjfaqjoejc14elz4xk8s/1300_850_1/wide_4_3_821a7b2af4c4914631b84d86a6cafaad.webp', 250, 0, 0, 100)
print(sugar)

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
