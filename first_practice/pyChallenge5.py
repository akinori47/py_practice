import pickle
from urllib import request

url = "http://www.pythonchallenge.com/pc/def/banner.p"
page = request.urlopen(url)
content = page.read().decode()
page.close()
result = pickle.load(content)
print(result)