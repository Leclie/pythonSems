# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

try:
    n = int(input("Введите количество монеток: "))
    count_0 = 0
    count_1 = 0
    for i in range(n):
        x = int(input("Введите сторону монетки (0 - решка, 1 - герб): "))
        if x == 0:
            count_0 += 1
        elif x == 1:
            count_1 += 1
        else:
            print("Вы ввели некоректные данные")
    if count_0 < count_1:
        print("Нужно перевернуть", count_0)
    else:
        print("Нужно перевернуть", count_1)
except:
    print("Вы ввели некоректные данные")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

try:
    s = int(input("Введите сумму чисел: "))
    p = int(input("Введите произведение чисел: "))
    N = 1000

    for i in range(N):
        for j in range(N):
            if i + j == s and i * j == p:
                print("X =", i, " Y =", j)
                print()
except:
    print("Вы ввели некоректные данные")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

try:
    n = int(input("Введите число N: "))
    num = 1

    while num < n:
        print(num)
        num *= 2
except:
    print("Вы ввели некоректные данные")


