import re

#----------Виклик функції для нормалізації номерівб Regex-----------
def normalize_phone(phone_number):
    number_re_list=re.sub(r"\D","",phone_number)
    formated=re.sub(r'^(?:38|8)?0?(\d{9})$', r'+380\1', number_re_list)
    return formated

#--------Тестові данні------------------
if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

#----------Викклик фуункції---------------
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

#---------Виведення нормалізований номерів-------
print(f"Нормалізовані номери телефонів для SMS-розсилки:, {sanitized_numbers}")
