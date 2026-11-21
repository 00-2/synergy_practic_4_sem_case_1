from calendar import isleap
from datetime import date

WEEKDAYS = (
    "понедельник", "вторник", "среда", "четверг",
    "пятница", "суббота", "воскресенье",
)
DIGITS = {
    "0": ("***", "* *", "* *", "* *", "***"),
    "1": (" * ", "** ", " * ", " * ", "***"),
    "2": ("***", "  *", "***", "*  ", "***"),
    "3": ("***", "  *", "***", "  *", "***"),
    "4": ("* *", "* *", "***", "  *", "  *"),
    "5": ("***", "*  ", "***", "  *", "***"),
    "6": ("***", "*  ", "***", "* *", "***"),
    "7": ("***", "  *", "  *", "  *", "  *"),
    "8": ("***", "* *", "***", "* *", "***"),
    "9": ("***", "* *", "***", "  *", "***"),
}


def weekday_name(birthday: date) -> str:
    return WEEKDAYS[birthday.weekday()]


def is_leap_year(year: int) -> bool:
    return isleap(year)


def age_in_years(birthday: date, today: date) -> int:
    before_birthday = (today.month, today.day) < (birthday.month, birthday.day)
    return today.year - birthday.year - int(before_birthday)


def render_birthday(birthday: date) -> str:
    groups = (f"{birthday.day:02d}", f"{birthday.month:02d}", f"{birthday.year:04d}")
    return "\n".join(
        "   ".join(" ".join(DIGITS[digit][row] for digit in group) for group in groups)
        for row in range(5)
    )


def main() -> None:
    today = date.today()
    while True:
        try:
            day = int(input("День рождения: "))
            month = int(input("Месяц рождения: "))
            year = int(input("Год рождения: "))
            birthday = date(year, month, day)
        except ValueError:
            print("Введите существующую дату целыми числами.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nВвод завершён.")
            return

        if birthday > today:
            print("Дата рождения не может быть в будущем.")
            continue
        break

    print(f"День недели: {weekday_name(birthday)}")
    print(f"Високосный год: {'да' if is_leap_year(birthday.year) else 'нет'}")
    print(f"Возраст (полных лет): {age_in_years(birthday, today)}")
    print("Дата рождения:")
    print(render_birthday(birthday))


if __name__ == "__main__":
    main()
