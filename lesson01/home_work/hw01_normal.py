
__author__ = 'Коробов Евгений   Юрьевич'

import math

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
print("Решение задачи №1")
n = (input("Введите произвольное число : "))
x = 0
for i in n:
    if i == "1":
        if x < int(i):
            x = int(i)
    if i == "2":
        if x < int(i):
            x = int(i)
    if i == "3":
        if x < int(i):
            x = int(i)
    if i == "4":
        if x < int(i):
            x = int(i)
    if i == "5":
        if x < int(i):
            x = int(i)
    if i == "6":
        if x < int(i):
            x = int(i)
    if i == "7":
        if x < int(i):
            x = int(i)
    if i == "8":
        if x < int(i):
            x = int(i)
    if i == "9":
        if x < int(i):
            x = int(i)
    if i == "0":
        if x < int(i):
            x = int(i)
print("Максимальная цифра - ", x)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("Решение задачи №2 ")
a = (input("Введите значение: "), )
b = (input("Введите другое значение : "), )
print("Результат ввода : ", "a = ", a, "b = ", b)
a, b = b, a
print("Результат перестановки : ", "a = ", a, "b = ", b)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
print("Решение задачи №3")

print("Предлагаем вашему вниманию программу для решения квадратных уравнений!")
print(" Общий вид уравнений ax**2 + bx + c = 0.  Вам необходимо ввести значение коэффициентов.")

answer = ""
while answer != "N":
    answer = input("Хотите найти решение? Y / N :")
    if answer == "Y":
        a = int(input("Значение a: "))
        b = int(input("Значение b: "))
        c = int(input("Значение c: "))
        d = b**2 - 4*a*c
        if d < 0:
            print("У данного уравнения нет корней")
        elif d > 0:
            D = math.sqrt(d)
            x1 = (- b + D) / 2 * a
            x2 = (- b - D) / 2 * a
            print("Корни уравнения найдены : ", "x1 = ", x1, ", x2 = ", x2)
        else:
            x1 = (- b) / 2 * a
            print("Дискриминант данного уревнения равен 0 --> корень один: x = ", x1)

print("Всего доброго!")