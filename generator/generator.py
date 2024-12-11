import os.path
import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(10000, 100000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )


def generated_file():
    # path = rf'/Users/olle/PycharmProjects/aqa_ui_portfolio_project/filetest{random.randint(0, 999)}.txt'

    # Получаем путь к текущей папке
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Поднимаемся на один уровень вверх
    parent_dir = os.path.dirname(current_dir)

    # Формируем путь к файлу в папке на уровень выше
    path = os.path.abspath(os.path.join(parent_dir, f'filetest{random.randint(0, 999)}.txt'))

    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path

# надежнее использовать контекстный менеджер with с функцией open()
# def generated_file():
#     path = rf"C:\python_projects\pet_project_aqa\filetest{random.randint(0, 777)}.txt"
#     with open(path, "w+") as my_file:
#         my_file.write(f"Hello world{random.randint(0, 777)}")
#
#     return my_file.name, path
