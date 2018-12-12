# practice some collatz operation
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


print("Введите число для построения последовательнсоти Коллатца:")
try:
    i = int(input())
except ValueError:
    print("ОШИБКА!!! Введите число")
else:
    while i > 1:
        i = collatz(i)