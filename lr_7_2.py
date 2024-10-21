def count_words_starting_with_letter(file_path, letter):
    # Приводим букву к нижнему регистру для учета регистра
    letter = letter.lower()

    # Переменная для подсчета слов
    count = 0

    # Открываем файл и читаем его содержимое
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # Разделяем текст на слова
        words = text.split()

        # Подсчитываем слова, начинающиеся с указанной буквы
        for word in words:
            # Убираем знаки препинания и приводим слово к нижнему регистру
            clean_word = ''.join(filter(str.isalpha, word)).lower()
            if clean_word.startswith(letter):
                count += 1

    return count

# Пример использования функции
file_path = 'text_7.txt'  # Укажите путь к вашему файлу
letter = 'н'  # Укажите букву для подсчета

result = count_words_starting_with_letter(file_path, letter)
print(f"Количество слов, начинающихся с буквы '{letter}': {result}")
