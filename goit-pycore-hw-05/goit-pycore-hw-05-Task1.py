def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            cache[0] = 0
        if n == 1:
            cache[n] = 1
        if n in cache:
            cache[n] = cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
# КІНЕЦЬ ФУНКЦІЇ caching_fibonacci
if __name__ == "__main__":
# Отримуємо функцію fibonacci
    fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610

