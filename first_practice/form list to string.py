# Зяпатая в качестве разделителя


spam = ['apple', 'banana', 'tofu', 'cats']


def dot(spisok):  # Функция переводит список в строку с запятой в качестве разделителя
    spisok = ', '.join(spisok)
    return spisok


print(dot(spam))
print(type(dot(spam)))
