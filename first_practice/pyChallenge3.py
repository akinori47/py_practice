from urllib import request

page = request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

contents = page.read()
page.close()

print(page.getheaders())


print(request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").getheader('Server'))
