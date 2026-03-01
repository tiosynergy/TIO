#------ створюємо генератор який знаходить числа в тексті, отримує аргумент text
def generator_numbers(text: str) -> Generator[float]:
    for word in text.split():  # Розбиваємо текст через пробіли на слова
        try:
        #--- Пробуємо чи слово є float; якщо так - видаємо число через yield
            yield float(word)
        #----# Якщо слово не число ігнор та нове коло
        except ValueError:
            pass

#------ функція сумування чисел витянутих герератором -------------
# def sum_profit(text: str, func: Callable[[str], Generator[float]]) -> float:
def sum_profit(text: str, func) -> float:
    # Викликаємо передану функцію func з текстом і сумуємо результат генератора
    return sum(func(text))  # sum() автоматично ітерує по генератору і додає числа


if __name__ == "__main__":

    #------- вхідні данні text -------
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    
    #---- Викликаємо sum_profit з текстом і generator_numbers як функція
    total_income = sum_profit(text, generator_numbers)
    
    #----- Виводимо результат
    print(f"Загальний дохід: {total_income}")