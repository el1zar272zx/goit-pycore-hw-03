"""Завдання 1: get_days_from_today."""

from datetime import datetime


def get_days_from_today(date: str):
    """Повертає кількість днів від заданої дати ('РРРР-ММ-ДД') до сьогодні.

    Якщо дата пізніша за поточну, результат від'ємний.
    Якщо формат невірний, повертає None.
    """
    try:
        given = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        print(f"Невірний формат дати: {date!r}. Очікується 'РРРР-ММ-ДД'.")
        return None
    today = datetime.today().date()
    return (today - given).days


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("09-10-2021"))
