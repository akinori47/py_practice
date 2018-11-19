# COMMENT

catNames = []
while True:
    print('Enter the name ' + str(len(catNames) + 1))
    name = input()
    if name == '':
        break
    catNames += [name]
print('The manes are:')
for name in catNames:
    print (' ' + name)