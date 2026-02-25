#----------открывается файл для чтения--------
def total_salary(path:str)->tuple:
    try:
        with open(path, 'r+', encoding="utf-8") as file:
            workers_list:list=[]

        #---------построчно читается содеримое файла----------
            lines=file.readlines()
            total_amount:float=0
            everage_amount:float=0

        #------для каждой строчки убираются, переносы, пробелы
        # ------- и через "," формируются списки---------
            for line in lines:
                cleaned_content=line.strip().split(",")

        #-------строка аппендится в список------
                workers_list.append(cleaned_content)

        #-------из списка где есть пара ключ-значение формируется словарь------
                workers_dict=dict(workers_list)

        #------ вибыирем значения ключей (values) и делаем точные вычисления-------
            for amount in workers_dict.values():
                total_amount+=float(amount)
                everage_amount=float(total_amount/len(workers_list))
                result=(total_amount,everage_amount)
        return result
    #--------обработка ошибки, есл файл не найден-----------
    except FileNotFoundError:
        print(f"файл {path} не знайдено")
        return (None, None)

# конструкция прямого вызова--------
if __name__ == "__main__":
    #-------Вызов функции-------------
    total,average=total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
