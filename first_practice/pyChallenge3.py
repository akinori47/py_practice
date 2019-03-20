# Python Challenge #3

from urllib import request
import string

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
page = request.urlopen(url)
contents = page.read()
page.close()
mess = contents.split
print(contents)
print(type(contents))