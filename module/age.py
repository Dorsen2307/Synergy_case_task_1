from datetime import date

def get_age(day, month, year):
    """ Возвращает количество лет """
    today = date.today()

    return today.year - year - ((today.month, today.day) < (month, day))