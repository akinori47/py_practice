# Python Challenge #3

from urllib import request


url = 'http://www.pythonchallenge.com/pc/def/equality.html'
page = request.urlopen(url)
contents = page.read()
page.close()
mess = contents.split(b'<!--\n')[-1]

print(mess)
print(type(mess))
