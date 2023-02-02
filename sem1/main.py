import math

"""
# Задача 1

try:
    n = int(input("Введите расстояние машины за день: "))
    m = int(input("Введите расстоние, которое надо преодолеть: "))
    res = math.ceil(m/n)
    print("Необходимо ", res, " дней")
except:
    print("Вы ввели некоректные данные")
print()

# Задача 2

print("Введите количество учащихся трех классов")
print()
try:
    a = int(input("1й класс: "))
    b = int(input("2й класс: "))
    c = int(input("3й класс: "))
    res = math.ceil((a+b+c)/2)
    print("Необходимо ", res, " парт")
except:
    print("Вы ввели некоректные данные")

print()
"""

# Задача 5

try:
    i = int(input("Введите расстояние машины за день: "))
    j = int(input("Введите расстоние, которое надо преодолеть: "))
    if i==j:
        print("без дополнительной информации это сделать невозможно")
    else:
        res = i + j - 1
        print("В поезде ", res, "вагонов")

except:
    print("Вы ввели некоректные данные")

print()


# Задача 7

try:
    y = int(input("Введите год: "))
    if y%4==0 and y%100!=0 or y%400==0:
        print("YES")
    else:
        print("NO")

except:
    print("Вы ввели некоректные данные")