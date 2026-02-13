import random

#-----------Введення та перевірка типів вхідних данних------
while True:
    try:
        min_digit=int(input("Введи мінімальне число >=1:"))
        if type(min_digit)==False:
            continue
        else:
            break
    except ValueError:
        print("Помилка: Потрібно вводити тільки цифри!")

while True:
    try:
        max_digit=int(input("Вееди максимальне число <=1000:"))
        if type(max_digit)==False:
            continue
        else:
            break
    except ValueError:
        print("Помилка: Потрібно вводити тільки цифри!")
while True:
    try:
        qtt_digits=int(input(f"Введи необхідну кількість випадкових чисел в діапазоні до:{max_digit-min_digit}: "))
        if type(qtt_digits)==False:
            continue
        else:
            break
    except ValueError:
        print("Помилка: Потрібно вводити тільки цифри!")

# --------перевіряє обмеження та надає:
#  список випадкових чисел або порпожній список--------------    
def get_numbers_ticket(min, max, quantity) ->[]:
    if min>=1 and min<max<1000 and min<=quantity<=max:
        digit_random_list=random.sample(range(min,max),quantity)
    else:
        digit_random_list=[]
    return digit_random_list


# ------------ Виклик Функції---------------
print(f"Набір унікальних випадкових чисел {get_numbers_ticket(min_digit,max_digit,qtt_digits)}")
