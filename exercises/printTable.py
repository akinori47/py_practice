table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(items):
    col_width = [int(0)] * len(items)
    print(col_width)
   #for i in items:
   #    for y in i:
   #        if len(items[i][y]) > col_width[y]:
   #            col_width[y] = len(items[i][y])
   #print(col_width)


print_table(table_data)