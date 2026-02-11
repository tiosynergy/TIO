import random

while True:
    min_digit=int(input("Вееди мінімальне число >=1:"))
    if min_digit>=1:
        break
while True:
    max_digit=int(input("Вееди максимальне число <=1000:"))
    if max_digit>min_digit and max_digit<=1000:
        break
while True:
    qtt_digits=int(input(f"Вееди необхідну кількість ввипадкових чисел в діапазоні до:{max_digit-min_digit}: "))
    if qtt_digits<=max_digit-min_digit:
        break
def get_numbers_ticket(min, max, quantity):
    digit_random_list=random.sample(range(min,max),quantity)
    print(digit_random_list)

get_numbers_ticket(min_digit,max_digit,qtt_digits)







# min_digit=int(input("Вееди мінімальне число:"))

# while True:
#     # Запрашиваем ввод и преобразуем в целое число
#     number = int(input("Введите число (0 для выхода): "))
    
#     # Проверяем условие выхода
#     if number == 0:
#         print("Вы ввели ноль. Программа завершена.")
#         break
    
#     # Обработка числа
#     print(f"Вы ввели: {number}")


 
