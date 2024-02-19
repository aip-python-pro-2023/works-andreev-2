from typing import Optional

from pysondb import db

class Ingredient:
    # Поле - переменная в классе
    # Метод - функция в классе

    __id: int
    __name: str
    __description: str
    __type: str
    __picture: str
    __calories: float
    __proteins: float
    __fats: float
    __carbohydrates: float

    # Конструктор, вызывается при создании объекта класса Ingredient
    def __init__(self,
                 id: int,
                 name: str,
                 description: str,
                 ingredient_type: str,
                 picture: str,
                 calories: float,
                 proteins: float,
                 fats: float,
                 carbohydrates: float):
        self.__id = id
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
    def __eq__(self, other: 'Ingredient') -> bool:
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

    def get_json(self):
        return {
            'name': self.__name,
            'description': self.__description,
            'ingredient_type': self.__type,
            'picture': self.__picture,
            'calories': self.__calories,
            'proteins': self.__proteins,
            'fats': self.__fats,
            'carbohydrates': self.__carbohydrates,
        }


class IngredientsRepository:
    def __init__(self):
        self.__database = db.getDb('ingredients.json')

    def save(self, ingredient: Ingredient) -> None:
        self.__database.add(ingredient.get_json())

    def find(self, name: str) -> Optional[list[Ingredient]]:
        result = self.__database.reSearch('name', rf'{name}')
        return [Ingredient(**row) for row in result]


if __name__ == '__main__':
    carrot = Ingredient('Морковь', 'Вкусный и полезный овощ', 'Овощ', 'https://vkustorg.com/image/cache/Ovochi_frukty/1460024087-500x500.jpg', 150, 70, 10, 20)
    sugar = Ingredient('Сахар', 'Сладкая вещь, с которой не стоит перебарщивать', 'Бакалея', 'https://centrstomatologii.ru/upload/resize_cache/webp/iblock/8b9/fe1rhhjon2lrtjfaqjoejc14elz4xk8s/1300_850_1/wide_4_3_821a7b2af4c4914631b84d86a6cafaad.webp', 250, 0, 0, 100)

    ingredients_repository = IngredientsRepository()
    ingredients_repository.save(carrot)
    ingredients_repository.save(sugar)
