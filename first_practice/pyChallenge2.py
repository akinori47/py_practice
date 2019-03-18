# PythonChallenge №2

from urllib import request

page = request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

contents = page.read()
page.close()

mess = str(contents.split("-->", 1))
mess= mess.split("<!--\n", 1)

















#print(page.getheaders())
#print(request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").getheader('Server'))
