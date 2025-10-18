from dataclasses import dataclass

# Описываем структуру данных, которая будет использоваться для генерации тестовых пользователей
@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None

# 💡 @dataclass автоматически создает __init__, __repr__, и другие методы. Это удобно для хранения тестовых данных

@dataclass
class Color:
    color_name: list = None