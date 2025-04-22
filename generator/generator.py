import os
import random

from data.data import Person
from faker import Faker

# Создаем объект Faker с русской локализацией
faker_ru = Faker('ru_RU')

# Устанавливаем сид для повторяемости данных (опционально)
Faker.seed()
# Faker.seed(123)


def generated_person():
    # Генератор одного объекта Person со случайными данными
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(10_000, 100_000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file():
    # path = rf'/Users/olle/PycharmProjects/aqa_ui_portfolio_project/filetest{random.randint(0, 999)}.txt'

    # Генерирует файл со случайным содержимым, возвращает имя файла и путь к нему

    # Получаем путь к текущему файлу
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Переходим на уровень выше (в корень проекта)
    parent_dir = os.path.dirname(current_dir)

    # Генерируем уникальное имя файла
    path = os.path.abspath(os.path.join(parent_dir, f'filetest{random.randint(0, 999)}.txt'))

    # Создаем файл и записываем случайный текст
    with open(path, 'w+') as file:
        file.write(f'Hello World {random.randint(0, 999)}')

    return file.name, path


# надежнее использовать контекстный менеджер with с функцией open()
# def generated_file():
#     path = rf"C:\python_projects\pet_project_aqa\filetest{random.randint(0, 777)}.txt"
#     with open(path, "w+") as my_file:
#         my_file.write(f"Hello world{random.randint(0, 777)}")
#
#     return my_file.name, path

def generated_subject():
    # Возвращает случайный школьный предмет из списка
    subject_list = [
        "Hindi", "English", "Maths", "Physics", "Chemistry",
        "Biology", "Computer Science", "Commerce", "Accounting",
        "Economics", "Arts", "Social Studies", "History", "Civics"
    ]

    # return subject_list[random.randint(0, 12)]
    return random.choice(subject_list)
