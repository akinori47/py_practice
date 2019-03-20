# PythonChallenge №2

from urllib import request

page = request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

contents = page.read()
page.close()


f = open('content.txt', 'r')        # отрываем файл с содержанием html станицы челленджа
content = f.read()      # записываем содержимое файла в переменную

items = {}      # создаем пустой словарь
for item in content:        # считаем кол-во каждого символа в файле
    if item in items:
        items[item] = items[item] + 1
    else:
        items[item] = 1

if items[item] == 1:        # выводим символы встречающиеся 1 раз
    for item in items:
        print(item)

# answer = equality














#print(page.getheaders())
#print(request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").getheader('Server'))
