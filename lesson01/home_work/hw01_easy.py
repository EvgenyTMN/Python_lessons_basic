
__author__ = 'Коробов Евгений Юрьевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
n = (input("Введите произвольное число : "))
for i in n:
    if i == "1":
        print("1")
    if i == "2":
        print("2")
    if i == "3":
        print("3")
    if i == "4":
        print("4")
    if i == "5":
        print("5")
    if i == "6":
        print("6")
    if i == "7":
        print("7")
    if i == "8":
        print("8")
    if i == "9":
        print("9")
    if i == "0":
        print("0")


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input("Введите значение: ")
b = input("Введите другое значение : ")
print("Результат ввода : ", "a = ", a, "b = ", b)
c = a
a = b
b = c
print("Результат замены :")
print("a = ", a, "b = ", b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Введите пожалуйста Ваш возраст : "))
if age < 18:
    print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешен")