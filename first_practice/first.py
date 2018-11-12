# Python 3.6 practice file
name =''
number_of_try = 0
while name != 'your name':
    print('Type your name.')
    name = input()
    number_of_try += 1

    if number_of_try == 5:
        print('Превышено число попыток')
        break
print('GZ')
