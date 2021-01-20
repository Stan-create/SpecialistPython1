# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

print("На лугу пасется...")
n = int(input("Введите положительное число n "))
if n == 0:
    print(n, "коров")
elif n == 1:
    print(n, "корова")
elif 2 <= n <= 4:
    print(n, "коровы")
elif n >= 5:
    print(n, "коров")
else:
    print()
