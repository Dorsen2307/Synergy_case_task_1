from module.age import get_age
from module.check import is_leap_year
from module.day_of_week import get_day_of_week
from module.input import select_menu_item, input_birthday
from module.output import output_menu, get_text_for_digits, print_date, print_all

fl_exit = True
while fl_exit:
    output_menu() # выводим меню
    item_menu = select_menu_item()
    if item_menu == 1:
        year, month, day = input_birthday()
        print_date(get_text_for_digits(day, month, year))
    elif item_menu == 2:
        year, month, day = input_birthday()
        print(f"День недели {day}.{month}.{year}: {get_day_of_week(day, month, year)}")
    elif item_menu == 3:
        year, month, day = input_birthday(True)
        print(f"{year} год високосный." if is_leap_year(year) else f"{year} год НЕ високосный.")
    elif item_menu == 4:
        year, month, day = input_birthday()
        print(f"На сегодня вам {get_age(day, month, year)} лет.")
    elif item_menu == 5:
        print_all()
    else:
        fl_exit = False