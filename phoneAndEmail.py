#! python3
# phoneAndEmail.py - Находит телефонные номера и адреса электронной почты в буфер обмена.

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{1} | \+\d{1})            # код страны
    (\s | - | \.)?               # разделитель
    (\d{3})                      # территориальный код
    (\s | - | \.)?               # разделитель
    (\d{3})                      # первые три цифры
    (\s | - | \.)?               # разделитель
    (\d{4})                      # последние 4 цифры
    )''', re.VERBOSE)

# Создание регулярного выражения для адресов электронной почты.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # 1 имя пользователя
    @                      # 2 символ @
    [a-zA-Z0-9.-]+         # 3 имя домена
    (\.[a-zA-Z]{2,4})      # остальная часть адреса
    )''', re.VERBOSE)

# Поиск соответствий в тексте, содержащемся в буфере обмена.
text = str(pyperclip.paste())

# 1
matches = []

# 2
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5], groups[7]])
    matches.append(phoneNum)

# 3
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Копирование результатов в буфер обмена.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты не обнаружены.')



















