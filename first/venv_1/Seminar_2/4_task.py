# ------------------------------------------- 3 -----------------------------
# Напишите программу, которая получает целое число
# и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.

# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

BIN: int = 2
OCT: int = 8

num: int = int(input('Введите число: '))

for div in [BIN, OCT]:
    test_num: int = num
    result: str = ''
    while test_num > 0:
        result = str(test_num % div) + result
        test_num //= div
    print(f'For {div} {result = }')

print(f'{bin(num) = :>15}\n{oct(num) = :>15}')

# ------------------------------------------- 4 -----------------------------
# Напишите программу, которая вычисляет площадь круга и
# длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# ------------------- 1

import math
import decimal

decimal.getcontext().prec = 50
PI = decimal.Decimal(math.pi)

diameter = decimal.Decimal(input('Введите диаметр: '))

length = PI * diameter
square = PI * (diameter / 2) ** 2

print(f'{length = }')
print(f'{square = }')

# ------------------- 2

import math
import decimal

def calculate_circle_properties(diameter: decimal.Decimal) -> tuple[decimal.Decimal, decimal.Decimal]:
    decimal.getcontext().prec = 42
    radius = diameter / 2
    area = decimal.Decimal(math.pi) * radius ** 2
    circumference = decimal.Decimal(math.pi) * diameter
    return area, circumference


value = decimal.Decimal(input("Введите диаметр круга: "))
if 0 >= value > 1000:
    print("Ошибка: диаметр должен быть положительным числом, не превышающим 1000.")
else:
    answer_1, answer_2 = calculate_circle_properties(value)
    print("Площадь круга:", answer_1)
    print("Длина окружности:", answer_2)

