                                                                        # дана строка, необходимо найти общее количество русских символов
import re
from datetime import datetime

string0 = "TEST ntcn тест ТЕСТ test"
russian_chars = re.findall(r'[а-яА-Я]', string0)
print(len(russian_chars))

                                                                        # дана строка, необходимо проверить образуют ли строчные символы латиницы палиндром

def palindrom(s):
    f_char = ''.join(c for c in s if 'a' <= c <= 'z' and c != ' ')
    # print(f_char)
    return f_char == f_char[::-1]

string1 = "a man a Plan a canal Panama"

print(palindrom(string1))

                                                                        # найти в тексте даты формата "день.месяц.год"
def find_dates(text):
    date_pattern = r'\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b'
    matches = re.findall(date_pattern, text)
    dates = []
    for day, month, year in matches:
        try:
            date = datetime.strptime(f"{day}.{month}.{year}", "%d.%m.%Y")
            dates.append(date)
        except ValueError:
            continue
    return dates

text = "Сегодня 31.12.2023, а завтра 01.01.2024. В прошлом году была дата 02.12.2022."
found_dates = find_dates(text)

for date in found_dates:
    print(date.strftime("%d.%m.%Y"))
