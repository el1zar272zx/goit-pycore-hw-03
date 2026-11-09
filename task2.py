"""Завдання 2: get_numbers_ticket."""

import random


def get_numbers_ticket(min, max, quantity):
    """Повертає відсортований список унікальних випадкових чисел.

    Обмеження: 1 <= min <= max <= 1000, 1 <= quantity <= max - min + 1.
    Якщо параметри некоректні, повертає порожній список.
    """
    if not all(isinstance(x, int) for x in (min, max, quantity)):
        return []
    if not (1 <= min <= max <= 1000):
        return []
    if not (1 <= quantity <= max - min + 1):
        return []
    return sorted(random.sample(range(min, max + 1), quantity))


if __name__ == "__main__":
    print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))
    print(get_numbers_ticket(0, 49, 6))
