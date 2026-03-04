def is_leap_year(year):
    """ Проверяет високосный ли год"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def check_date(value, part_of_date, month):
    """ Проверяет корректность введенных данных """
    month_31 = [1, 3, 5, 7, 8, 10, 12]

    if part_of_date == 'год':
        return 3 < len(value) < 5
    elif part_of_date == 'месяц':
        return 0 < int(value) < 13
    elif part_of_date == 'день':
        return 0 < int(value) < 31 if month in month_31 else 0 < int(value) < 30