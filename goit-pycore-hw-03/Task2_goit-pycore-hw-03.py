import random


def get_numbers_ticket(min, max, quantity) -> list:
    """перевіряє обмеження та надає:
       список випадкових чисел або порпожній список"""
    if (
        1 <= min
        and min < max <= 1000
        and min <= quantity <= max
    ):
        return random.sample(range(min, max + 1), quantity)
    return []


#-----------Введення та перевірка типів вхідних данних------
if __name__ == "__main__":
    while True:
        try:
            min_digit = int(input("Введи мінімальне число >= 1:"))
            if type(min_digit) == False:
                continue
            else:
                break
        except ValueError:
            print("Помилка: Потрібно вводити тільки цифри!")

    while True:
        try:
            max_digit = int(input("Вееди максимальне число <=1000:"))
            if type(max_digit) == False:
                continue
            else:
                break
        except ValueError:
            print("Помилка: Потрібно вводити тільки цифри!")
    while True:
        try:
            request_text = f"Введіть кількість чисел (до {max_digit - min_digit}): "
            qtt_digits = int(input(request_text).strip())
            if type(qtt_digits) == False:
                continue
            else:
                break
        except ValueError:
            print("Помилка: Потрібно вводити тільки цифри!")


# ------------ Виклик Функції---------------
    result = get_numbers_ticket(min_digit, max_digit, qtt_digits)
    print(f"Набір унікальних випадкових чисел {result}")
