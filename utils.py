"""Утилиты приветствия демо-проекта GitPractice."""


def greet(name):
    """Возвращает приветствие для указанного имени."""
    return "Привет, " + name + "!"


def farewell(name):
    """Возвращает прощание для указанного имени."""
    return "Пока, " + name + "!"


if __name__ == "__main__":
    print(greet("мир"))
    print(farewell("мир"))
