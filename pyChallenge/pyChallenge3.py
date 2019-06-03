# Python Challenge №3
from urllib import request
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
page = request.urlopen(url)
contents = page.read().decode()
page.close()
mess = contents.split('<!--\n')[-1].split('-->\n')[0]
pattern = re.compile('[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+')
result = "".join(pattern.findall(mess))
print(result)
