import re

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

def validate_email(email):
    if not is_valid_email(email):
        raise ValueError("Некорректный адрес электронной почты.")
    return email

try:
    email = "example@example.com"
    print(f"Адрес '{email}' является корректным: {is_valid_email(email)}")  # True
    print(f"Валидированный адрес: {validate_email(email)}")  # example@example.com

    email = "invalid-email@.com"
    print(f"Адрес '{email}' является не корректным: {is_valid_email(email)}")  # False
    print(f"Валидированный адрес: {validate_email(email)}")  # Это вызовет исключение
except ValueError as e:
    print(e)
