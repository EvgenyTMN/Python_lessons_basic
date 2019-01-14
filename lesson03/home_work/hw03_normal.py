# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = [1, 1, ]
    x1 = fib[0]
    x2 = fib[1]
    for x in range(m):
        x3 = x2 + x1
        fib.append(x3)
        x1 = x2
        x2 = x3
    n = n - 1
    s = fib[n:m]
    return s

print(fibonacci(1, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    stm = []
    for x in range(len(origin_list)):
        m = min(origin_list)
        stm.append(m)
        origin_list.remove(m)
    return stm


a = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]

print(sort_to_max(a))

def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list [i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list



a = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(sort_to_max(a))



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

