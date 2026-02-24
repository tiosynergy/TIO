import sys
from pathlib import Path
import colorama
from colorama import Fore, Style, init


init(autoreset=True)

# функция сортировки файл- True или папка - False + имя
def sort_key(x):
    return (x.is_file(), x)

# фуункция вывода структуры директории
def tree(path: Path, space: str = '', level: int = 0):

# Проверка на существование дирректории
    try:
# составляем и сортирууем список папок и файлов
        items = sorted(path.iterdir(), key=sort_key)
    except FileNotFoundError:
        print('Директория не найдена')
        return
    
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        if item.is_dir():
            print(space + Fore.BLUE + item.name + '/' + Style.RESET_ALL)
            new_space = space + ('  ' if is_last else '    ')
            tree(item, new_space, level + 1)
        else:
            print(space + Fore.GREEN + item.name + Style.RESET_ALL)

if __name__ == '__main__':

    dir_path = sys.argv[1]
    p = Path(dir_path)
    
    print(f"Структура директории: {p.absolute()}")
    # ------- вызов функции------
    tree(p)
    


# python D:\OneDrive\Desktop\Python\Neoversity\TEST\TIO\goit-pycore-hw-04-Task3\goit-pycore-hw-04-Task3.py D:\OneDrive\Desktop\Python\Neoversity\Practice

