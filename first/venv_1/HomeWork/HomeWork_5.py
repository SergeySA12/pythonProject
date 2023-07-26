# Задача №6
# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.


def mult_table():
    LOWER_LIMIT = 2
    UPPER_lIMIT = 10
    COLUMN = 4
    print(' ', end='')
    print(*(f'{k:>} x {j:>2} = {k * j:>2}\n\n' if j == UPPER_lIMIT and k == i + COLUMN - 1 else \
                f'{k:>} x {j:>2} = {k * j:>2}\n' if k == i + COLUMN - 1 else \
                    f'{k:>} x {j:>2} = {k * j:>2}\t\t' \
            for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN)
            for j in range(LOWER_LIMIT, UPPER_lIMIT + 1)
            for k in range(i, i + COLUMN)))


mult_table()


def product_table() -> iter:
    LOWER_LIMIT = 2
    UPPER_lIMIT = 10
    COLUMN = 4

    for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN):
        for j in range(LOWER_LIMIT, UPPER_lIMIT + 1):
            for k in range(i, i + COLUMN):
                if j == UPPER_lIMIT and k == i + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n\n', end='')
                elif k == i + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n', end='')
                else:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\t\t', end='')


product_table()

# Задача №1
# Напишите функцию, которая принимает
# на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_file_path(path):
    # Разделяем абсолютный путь на путь к директории и имя файла
    dir_path, full_filename = path.rsplit("/", 1)

    # Делим имя файла на имя и расширение
    name, file_ext = full_filename.split(".", 1)

    return dir_path, name, f".{file_ext}"


file_path = '/home/user/documents/example.txt'
directory, filename, file_extension = split_file_path(file_path)
print("Путь:", directory)
print("Имя файла:", filename)
print("Расширение файла:", file_extension)


# Задача №2
# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем
# в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Валерий', 'Артур', 'Андрей', 'Василий']
salary = [15000, 20000, 18000, 50000]
bonus = ['10.25%', '15.00%', '18.50%', '12.05%']


def salary_gen(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: float]:
    return {name: sale / 100 * bon for name, sale, bon in zip(names, salary, (float(i[:-1]) for i in bonus))}.items()


print(*(salary_gen(names, salary, bonus)))

# Задача №3
# Создайте функцию генератор чисел Фибоначчи
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


num_terms = 10
fibonacci_sequence = list(fibonacci_generator(num_terms))
print(fibonacci_sequence)

