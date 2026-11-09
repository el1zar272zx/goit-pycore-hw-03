"""Завдання 4: get_upcoming_birthdays."""

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """Повертає список привітань на найближчі 7 днів (включно з сьогодні).

    Якщо день народження випадає на вихідний, привітання переноситься
    на наступний понеділок.
    """
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        try:
            this_year = birthday.replace(year=today.year)
        except ValueError:  # 29 лютого у невисокосний рік
            this_year = birthday.replace(year=today.year, month=3, day=1)

        if this_year < today:
            try:
                this_year = this_year.replace(year=today.year + 1)
            except ValueError:
                this_year = this_year.replace(year=today.year + 1, month=3, day=1)

        if 0 <= (this_year - today).days <= 7:
            congrats = this_year
            if congrats.weekday() >= 5:  # субота або неділя
                congrats += timedelta(days=7 - congrats.weekday())
            result.append(
                {"name": user["name"],
                 "congratulation_date": congrats.strftime("%Y.%m.%d")}
            )
    return result


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]
    print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
