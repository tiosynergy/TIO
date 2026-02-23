import pathlib, sys


# Проверяем, есть ли аргументы
if len(sys.argv) > 1:
    print("Переданные аргументы:")
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("Аргументы не переданы.")


#   D:\OneDrive\Desktop\Python\Neoversity\TEST
# goit-pycore-hw-04-Task3\goit-pycore-hw-04-Task3.py
# D:\OneDrive\Desktop\Python\Neoversity\TEST\TIO\goit-pycore-hw-04-Task3\goit-pycore-hw-04-Task3.py
# python D:\OneDrive\Desktop\Python\Neoversity\TEST\TIO\goit-pycore-hw-04-Task3\goit-pycore-hw-04-Task3.py arg1 arg2 "arg with space"