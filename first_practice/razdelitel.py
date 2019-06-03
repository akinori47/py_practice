spam = ["A", "B", "C", "D"]
print (spam[:-1])


def razdelitel (spisok):
    new_line = ', '.join(spisok[:-1]) + (' and ' + spisok[-1])
    print(new_line)


razdelitel(spam)