from module.check import check_date

def input_user(part_of_date, text, month=31):
    """ Ввод пользователя """
    value = input(text)

    if value.isdigit():
        if check_date(value, part_of_date, month):
            return int(value)

    print(f'Некорректный ввод "{part_of_date}". Пожалуйста повторите.')
    return input_user(part_of_date, text, month)


def input_birthday(leap=False):
    """ Инициализация ввода дня рождения или года"""
    month_of_birth = None
    birthday = None

    year_of_birth = input_user('год', 'Введите год рождения: ')
    if not leap:
        month_of_birth = input_user('месяц', 'Введите месяц рождения: ')
        birthday = input_user('день', 'Введите число рождения: ', month_of_birth)

    return year_of_birth, month_of_birth, birthday


def select_menu_item():
    """ Выбор пункта меню """
    value = input('Выберите пункт: ')

    if value.isdigit():
        return int(value) if 1 <= int(value) <= 5 else 0

    print(f'Некорректный ввод". Повторите.')
    return select_menu_item()