# -*- coding: utf-8 -*-
# coding python 3.6


class b_colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'


def multi_table():
    for i in range(1, 10):
        for j in range(1, 10):
            if (i * j) % 2 == 0:       #Условие для вывода четных и нечетных чисел разными цветами
                print(b_colors.OKBLUE + str(i * j) + b_colors.ENDC, end="\t")
            else:
                print(b_colors.OKGREEN + str(i * j) + b_colors.ENDC, end="\t")
        print()


multi_table()










