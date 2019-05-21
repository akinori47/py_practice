# Python Challenge №4

from urllib import request
import re


base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
pattern = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
base = str(12345)

for i in range(400):
    %timeit
    page = request.urlopen(pattern + base)
    content = page.read().decode()
    page.close()
    base = "".join(re.findall(r'\d', content))
    print(content)
