# Синьков Дмитрий Вадимович, группа 39/1
# ========================================================================
# Вариант 11
# ========================================================================
# В генеалогическом древе у каждого человека, кроме родоначальника,
# есть ровно один родитель. Каждом элементу дерева сопоставляется целое
# неотрицательное число, называемое высотой. У родоначальника высота равна
# 0, у любого другого элемента высота на 1 больше, чем у его родителя.
# Вам дано генеалогическое древо, определите высоту всех его элементов.
# Программа получает на вход число элементов в генеалогическом древе
# N . Далее следует N -1 строка, задающие родителя для каждого элемента
# древа, кроме родоначальника. Каждая строка имеет вид имя_потомка
# имя_родителя.
# Программа должна вывести список всех элементов древа в
# лексикографическом порядке. После вывода имени каждого элемента
# необходимо вывести его высоту.
# _______________________________________
# |Ввод                 |Вывод          |
# |_____________________|_______________|
# |9                    |               |
# |Alexei Peter_I       |Alexander_I 4  |
# |Anna Peter_I         |Alexei 1       |
# |Elizabeth Peter_I    |Anna 1         |
# |Peter_II Alexei      |Elizabeth 1    |
# |Peter_III Anna       |Nicholaus_I 4  |
# |Paul_I Peter_III     |Paul_I 3       |
# |Alexander_I Paul_I   |Peter_I 0      |
# |Nicholaus_I Paul_I   |Peter_II 2     |
# |                     |Peter_III 2    |
# |_____________________|_______________|

def main():
    from collections import defaultdict

    filename = 'test.txt'

    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().splitlines()

    N = int(data[0])  # Число элементов
    parent_dict = {}
    children_dict = defaultdict(list)

    # Считываем пары потомок-родитель
    for i in range(1, N):
        descendant, parent = data[i].split()
        parent_dict[descendant] = parent
        children_dict[parent].append(descendant)

    # Находим родоначальника (чей родитель не указан)
    all_descendants = set(parent_dict.keys())
    all_parents = set(parent_dict.values())
    root = list(all_parents - all_descendants)

    if root:
        root = root[0]  # Получаем родоначальника, если он найден
    else:
        print("Родоначальник не найден!")
        return

    # Словарь для хранения высот
    heights = {}

    # Функция для вычисления высоты
    def calculate_height(node, height):
        heights[node] = height
        for child in children_dict[node]:
            calculate_height(child, height + 1)

    # Начинаем с родоначальника
    calculate_height(root, 0)

    # Сортируем имена в лексикографическом порядке
    sorted_names = sorted(heights.keys())

    # Выводим имена и их высоты
    for name in sorted_names:
        print(f"{name} {heights[name]}")

if __name__ == "__main__":
    main()
