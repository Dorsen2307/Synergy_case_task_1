from module.age import get_age
from module.check import is_leap_year
from module.day_of_week import get_day_of_week
from module.input import input_birthday


def output_menu():
    """ Выводит меню """
    print(
    '''
    ======= Кейс-задача №1 =======
    
    1 - Стилистическая дата
    2 - День недели
    3 - Високосный ли год?
    4 - Сколько лет?
    
    5 - Вся информация
    
    ВЫХОД - любое число
    '''
    )


def get_text_for_digits(day, month, year):
    """ Конвертирует дату в текст """
    return f"{day}.{month}.{year}"


def print_date(date_str):
    """ Выводит дату в стиле цифрового табло звёздочками """

    # Сегментный индикатор в стиле "звёздочки"
    digits = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "*   *", "   * ", "  *  ", "*****"],
        '3': [" *** ", "*   *", "  ** ", "*   *", " *** "],
        '4': ["*   *", "*   *", "*****", "    *", "    *"],
        '5': ["*****", "*    ", "**** ", "    *", "**** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", "  *  "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "],
        '-': ["     ", "     ", "*****", "     ", "     "],
        ':': ["     ", "  *  ", "     ", "  *  ", "     "],
        '/': ["     ", "    *", "   * ", "  *  ", "*    "],
        '.': ["     ", "     ", "     ", "     ", "  *  "],
    }

    # Собираем все строки
    result = [""] * 5

    for char in date_str:
        if char in digits:
            pattern = digits[char]
            for i in range(5):
                result[i] += pattern[i] + "  "
        else:
            # Пропускаем неподдерживаемые символы
            for i in range(5):
                result[i] += "     " + "  "

    # Выводим результат
    for line in result:
        print(line)


def print_all():
    year, month, day = input_birthday()
    print()
    print('=' * 50)
    print(f"День недели {day}.{month}.{year}: {get_day_of_week(day, month, year)}")
    print(f"{year} год високосный." if is_leap_year(year) else f"{year} год НЕ високосный.")
    print(f"На сегодня вам {get_age(day, month, year)} лет.")
    print_date(get_text_for_digits(day, month, year))
    print('=' * 50)