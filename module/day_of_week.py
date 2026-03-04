from module.check import is_leap_year

def get_day_of_week(day, month, year):
    """ Возвращает день недели """
    list_month_codes = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6] # коды месяцев
    list_month_codes_leap_year = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6] # коды месяцев в високосном году
    list_day_of_week = {
        0: 'суббота',
        1: 'воскресенье',
        2: 'понедельник',
        3: 'вторник',
        4: 'среда',
        5: 'четверг',
        6: 'пятница'
    }

    # Вычисляем код месяца в зависимости от года
    if is_leap_year(year):
        month_code = get_month_code(month, list_month_codes_leap_year)
    else:
        month_code = get_month_code(month, list_month_codes)

    # Вычисляем код года
    last_number_of_year = year % 100
    year_code = (6 + last_number_of_year + last_number_of_year // 4) % 7

    # Вычисляем день недели
    day_of_week = (day + month_code + year_code) % 7

    return list_day_of_week[day_of_week]


def get_month_code(month, list_month_codes):
    """ Возвращает код месяца на основе месяца """
    return list_month_codes[month - 1]