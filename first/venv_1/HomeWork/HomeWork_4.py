# ------------------------------------------- 1 -----------------------------
# Напишите функцию для транспонирования матрицы

from random import randint
from typing import List


def fill_matrix(rows: int, cols: int, min_val: int, max_val: int) -> List[List[int]]:
    return [[randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def display_matrix(mass: List[List[int]]) -> None:
    for r in mass:
        print(" ".join(str(element) for element in r))


def transpose_matrix(mass: List[List[int]]) -> List[List[int]]:
    rows = len(mass)
    cols = len(mass[0])

    # Создаем новую матрицу с обращенными размерами и заполняем значениями из исходной матрицы
    transposed_matrix = [[mass[j][i] for j in range(rows)] for i in range(cols)]

    return transposed_matrix


row, column = map(int, input().split())
start, stop = map(int, input().split())
matrix = fill_matrix(row, column, start, stop)
t_matrix = transpose_matrix(matrix)

display_matrix(matrix)
print()
display_matrix(t_matrix)


# ------------------------------------------- 2 -----------------------------
# Напишите функцию принимающую на вход только
# ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

from typing import Any, Dict, Union


def build_arg_dict(**kwargs: Any) -> Dict[Union[int, float, str, tuple, frozenset], str]:
    arg_dict: Dict[Union[int, float, str, tuple, frozenset], str] = {}
    for key, value in kwargs.items():
        if not isinstance(value, (int, float, str, tuple, frozenset)):
            value = str(value)
        arg_dict[value] = key
    return arg_dict


result = build_arg_dict(a=10, b=20, c=30.5, d="hello", e=[1, 2, 3], f={1: 11, 2: 22})
print(result)
