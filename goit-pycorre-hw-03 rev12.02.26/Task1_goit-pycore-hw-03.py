import datetime
from datetime import datetime


def get_days_from_today(date) -> int: 
    current_date=datetime.now().date()
    dlt=current_date-date.date()
    return dlt.days

# ----------- Перевірка введення року -------------
while True:
    try:
        input_year=int(input("Введіть рік: "))
        if type(input_year)==False:
            continue
        else:
            break
    except ValueError:
        print("Помилка: Потрібно вводити тільки цифри!")

# ---------- Перевірка введення місяця ----------------
while True:
    try:
        input_month=int(input("Введіть міяць: "))
        if type(input_month)==False or 0>= input_month >13:
            continue
        else:
            break
    except ValueError:
        print("Помилка: Потрібно вводити тільки цифри!")

# ------------- Перевірка введення дня ---------------
while True:
    try:
        input_day=int(input("Введіть день: "))
        if type(input_day)==False:
            continue
        else:
            break
    except ValueError:
        print("Помилка: Потрібно вводити тільки цифри!")


inputed_date=datetime(input_year,input_month,input_day)
current_date=datetime.today().date()

print(f"кількість днів між\n заданою датою: {inputed_date.date()}\n і поточною датою: {current_date} \n становить {get_days_from_today(inputed_date)}")
