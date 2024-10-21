def find_max_sum_segment(file_path):
    with open(file_path, 'r') as f:
        # Считываем первую строку
        first_line = f.readline().strip()
        N, K = map(int, first_line.split())

        # Считываем высоты
        heights = [int(f.readline().strip()) for _ in range(N)]

    # Префиксная сумма
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + heights[i - 1]

    max_sum = float('-inf')  # Начальное значение для максимальной суммы

    # Используем два указателя для поиска максимальной суммы
    for start in range(N):
        end = start + K  # Устанавливаем конец на K метров дальше от начала
        if end >= N:
            break  # Если конец выходит за границы массива, выходим из цикла

        current_sum = prefix_sum[end + 1] - prefix_sum[start]  # Сумма от start до end
        max_sum = max(max_sum, current_sum)

    return max_sum

# Пример вызова функции
file_test_7 = 'test7.txt'
file_path_a = '27-170a.txt'
file_path_b = '27-170b.txt'

max_sum_test = find_max_sum_segment(file_test_7)
print("Максимальная оценка для файла test7:", max_sum_test)

max_sum_a = find_max_sum_segment(file_path_a)
print("Максимальная оценка для файла A:", max_sum_a)

max_sum_b = find_max_sum_segment(file_path_b)
print("Максимальная оценка для файла B:", max_sum_b)

# 550
# 1254156
# 45076190
