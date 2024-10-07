# +++, Вариант 1, Группа 39.1
# Задачи 1 13 25 37 49

# Дан целочисленный массив, необходимо найти количество элементов, расположенных после последнего максимального.
def count_elements_after_last_max(arr):
    if not arr:  # Проверка на пустой массив
        return 0

    max_value = max(arr)  # Находим максимальное значение
    last_max_index = -1  # Инициализируем индекс последнего максимального

    # Ищем индекс последнего максимального элемента
    for i in range(len(arr)):
        if arr[i] == max_value:
            last_max_index = i

    # Если последний максимальный индекс не найден, возвращаем 0
    if last_max_index == -1:
        return 0

    # Количество элементов после последнего максимального
    return len(arr) - last_max_index - 1


# Дан целочисленный массив, необходимо разместить элементы, расположенные до минимального, в конец массива.
def move_elements_before_min_to_end(arr):
    if not arr:  # Проверка на пустой массив
        return arr

    # Находим индекс минимального элемента
    min_index = arr.index(min(arr))

    # Разделяем массив на две части
    before_min = arr[:min_index]  # Элементы до минимального
    after_min = arr[min_index:]    # Элементы от минимального до конца

    # Объединяем обе части
    return after_min + before_min


# Дан целочисленный массив, и интервал a..b. Необходимо найти максимальный из элементов в этом массиве.
def max_in_range(arr, a, b):
    # Инициализируем переменную для максимума
    max_value = None

    # Перебираем элементы массива
    for num in arr:
        if a <= num <= b:  # Проверяем, находится ли элемент в интервале
            if max_value is None or num > max_value:
                max_value = num  # Обновляем максимум

    return max_value


# Дан целочисленный массив. Вывести индексы элементов которые меньше своего левого соседа, и количество таких чисел.
def find_elements_smaller_than_left(arr):
    indices = []  # Список для хранения индексов
    count = 0     # Счетчик для количества элементов

    # Проходим по массиву начиная со второго элемента
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:  # Сравниваем с левым соседом
            indices.append(i)  # Добавляем индекс в список
            count += 1  # Увеличиваем счетчик

    return indices, count



# Для введённого списка положительных чисел построить список всех положительных простых делителей элементов списка без повторений.
def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def positive_prime_divisors(numbers):
    """Находит все уникальные положительные простые делители из списка положительных чисел."""
    prime_divisors = set()  # Используем множество для уникальности

    for number in numbers:
        # Находим делители числа
        for i in range(1, number + 1):
            if number % i == 0 and is_prime(i):
                prime_divisors.add(i)  # Добавляем только простые делители

    return sorted(prime_divisors)  # Возвращаем отсортированный список


# Цикл
if __name__ == "__main__":
    numbers = [5, 12, 3, 7, 19, 22, 15, 8, 6, 11, 20, 14, 9, 18, 2, 17, 4, 16, 10, 13]

    while True:
        print("Input array: ", numbers)
        print("1 = найти количество элементов, расположенных после последнего максимального")
        print("2 = разместить элементы, расположенные до минимального, в конец массива")
        print("3 = необходимо найти максимальный из элементов в этом массиве")
        print("4 = вывести индексы элементов которые меньше своего левого соседа, и количество таких чисел")
        print("5 = построить список всех положительных простых делителей элементов списка без повторений")
        print("exit = for exit \n")

        sw = input()
        print("Ответ")
        if sw == "1":
            print(count_elements_after_last_max(numbers))
        elif sw == "2":
            print(move_elements_before_min_to_end(numbers))
        elif sw == "3":
            print("Please enter the A and B values:")
            A = int(input())
            B = int(input())
            print(max_in_range(numbers, A, B))
        elif sw == "4":
            indices, count = find_elements_smaller_than_left(numbers)
            print("Indices:", indices)
            print("Count:", count)
        elif sw == "5":
            print(positive_prime_divisors(numbers))
        elif sw == "exit":
            exit()
        else:
            print("Please enter correct input!")
        print("\n")



