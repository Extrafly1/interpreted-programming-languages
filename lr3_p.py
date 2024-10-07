# вариант 1 +++
# задачи 1 4 7 10
# Отсортировать строки в указанном порядке

import re

# ===================================================================================
# В порядке увеличения разницы между средним количеством согласных и средним количеством гласных букв в строке.
def vowel_consonant_difference(s):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY"  # Гласные буквы
    consonants = "бвгджзйклмнптфхцчшщБВГДЖЗЙКЛМНПТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  # Согласные буквы

    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char in consonants)

    total_count = vowel_count + consonant_count
    if total_count == 0:
        return 0  # Если нет ни гласных, ни согласных, возвращаем 0

    average_vowels = vowel_count / total_count
    average_consonants = consonant_count / total_count

    return abs(average_consonants - average_vowels)

def sort_strings_by_difference(strings):
    return sorted(strings, key=vowel_consonant_difference)


# ===================================================================================
# В порядке увеличения квадратического отклонения среднего веса ASCII-кода символа строки от среднего веса ASCII-кода символа первой строки.
def average_ascii_weight(s):
    if len(s) == 0:
        return 0
    return sum(ord(char) for char in s) / len(s)

def quadratic_deviation(s, average_first):
    avg_current = average_ascii_weight(s)
    return (avg_current - average_first) ** 2

def sort_strings_by_quadratic_deviation(strings):
    if not strings:
        return strings

    average_first = average_ascii_weight(strings[0])
    return sorted(strings, key=lambda s: quadratic_deviation(s, average_first))


# ===================================================================================
# В порядке увеличения квадратичного отклонения между количеством сочетаний "гласная-согласная" и "согласная-гласная" в строке.
def is_vowel(char):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY"
    return char in vowels

def count_transitions(s):
    vowel_to_consonant = 0
    consonant_to_vowel = 0
    prev_char = None

    for char in s:
        if prev_char is not None:
            if is_vowel(prev_char) and not is_vowel(char):
                vowel_to_consonant += 1
            elif not is_vowel(prev_char) and is_vowel(char):
                consonant_to_vowel += 1
        prev_char = char

    return vowel_to_consonant, consonant_to_vowel

def quadratic_deviation(s):
    vowel_to_consonant, consonant_to_vowel = count_transitions(s)
    return (vowel_to_consonant - consonant_to_vowel) ** 2

def sort_strings_by_quadratic_deviation(strings):
    return sorted(strings, key=quadratic_deviation)


# ===================================================================================
# В порядке увеличения среднего количества "зеркальных" троек (например, "ada") символов в строке.
def clean_string(s):
    # Убираем все символы, кроме букв
    return re.sub(r'[^a-zA-Zа-яА-ЯёЁ]', '', s)

def count_palindromic_triplets(s):
    count = 0
    length = len(s)

    for i in range(length - 2):
        triplet = s[i:i+3]  # Берем тройку символов
        if triplet == triplet[::-1]:  # Проверяем, является ли тройка палиндромом
            count += 1

    return count

def average_palindromic_triplets(s):
    if len(s) < 3:
        return 0  # Если строка меньше 3 символов, палиндромов нет
    return count_palindromic_triplets(s) / (len(s) - 2)

def sort_strings_by_average_palindromic_triplets(strings):
    return sorted(strings, key=lambda s: average_palindromic_triplets(clean_string(s)))


# ===================================================================================
strings = [
    "Привет мир!",
    "Как дела?",
    "Python - это язык программирования.",
    "Сортировка строк.",
    "А роза упала на лапу Азора.",
    "Сказка о рыбаке и рыбке.",
    "Потерянный мир.",
    "Тот, кто не рискует, тот не пьет шампанское.",
    "А в лесу родилась ёлочка.",
    "Слон и Моська.",
    "Madam, in Eden, I'm Adam.",
    "Was it a car or a cat I saw?",
    "Step on no pets.",
    "A man, a plan, a canal: Panama.",
    "Далеко-далеко за словесными горами.",
    "На свете много чудес, и все они в нашей голове.",
    "Словно в сказке, да не в сказке.",
    "Время — лучший учитель, но, к сожалению, оно убивает своих учеников.",
    "Каждый день — это новая жизнь.",
    "На всякого мудреца довольно простоты.",
    "Язык — это не просто средство общения, это ключ к пониманию.",
    "Счастье — это не цель, а способ жизни."
]


print("\n")

sorted_strings0 = sort_strings_by_difference(strings)
for s in sorted_strings0:
    print(s)

print("\n ============ \n")


sorted_strings1 = sort_strings_by_quadratic_deviation(strings)
for s in sorted_strings1:
    print(s)

print("\n ============ \n")

sorted_strings2 = sort_strings_by_quadratic_deviation(strings)
for s in sorted_strings2:
    print(s)

print("\n ============ \n")
strings = [
    "ada",
    "abc",
    "racecar",
    "noon",
    "abba",
    "xyzzy",
    "a",
    "aaa"
]

sorted_strings3 = sort_strings_by_average_palindromic_triplets(strings)
for s in sorted_strings3:
    print(s)
