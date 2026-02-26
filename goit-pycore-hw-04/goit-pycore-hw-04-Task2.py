def get_cats_info(path:str) -> list:
    cats:list = []
#----------обработка ошибок с файлом----------
    try:
#----------открывается файл для чтения--------
        with open(path, 'r', encoding="utf-8") as file:
            for lines in file:
#-----очищаются данные для добавления в словарь-------
                cleaned_content = lines.strip().split(",")
                cats_dict:dict = {
                    "id":cleaned_content[0],
                    "name":cleaned_content[1],
                    "age":int(cleaned_content[2])}
#----формируется списокк из словарей----------
                cats.append(cats_dict)
        return cats
#-----обработка ошибки, если файл не найден-----------
    except FileNotFoundError:
        print(f"файл {path} не знайдено")


# конструкция прямого вызова--------
if __name__ == "__main__":
#------вызов функции------------
    cats_info:list = get_cats_info("cats.txt")
    print(cats_info)