# Задача № 1

""" def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number
def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum
num = InputNumbers("Введите число: ")
print(f"Сумма цифр = {sumNums(num)}") """


# Задача № 2

""" def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number
def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)
num = InputNumbers("Введите число: ")
list = []
for e in range(1, num + 1):
    list.append(mult(e))
print(f"Произведения чисел от 1 до {num}:  {list}") """

# Задача №3

""" Size = int(input("Введите размер списка: "))
result = list(range(-Size, Size+1))
print(result) """

# Задача №4

""" from math import prod
arr = [int(input('Введите элемент списка: ')) for i in range(int(input('Введите длину списка: ')))]
print(f'Весь список: {arr}')
print(f'Произведение элементов списка: {prod(arr)}') """

# Задача №5

""" import random
list = [input("Введите значения в список: ") for i in range(int(input('Введите длину списка: ')))]
print(f'Весь список: {list}')
random.shuffle(list)
print(list) """

# Задача №6

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number

k = InputNumbers("Введите число: ")
print(sum((1 + 1 / i) ** i for i in range(1, k + 1)))