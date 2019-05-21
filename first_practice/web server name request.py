from urllib import request

user_input = str(input("Enter URL:\t"))
print(request.urlopen(user_input).getheader('Server'))
