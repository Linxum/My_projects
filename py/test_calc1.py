import math
print("Поддерживается + - * / ^ Пи sqrt()")
func = input("Функция: ")
if func == "+":
    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))
    c = a + b
    print("Результат сложения: " + str(a) + " + " + str(b) + " = " + str(c))
elif func == "-":
    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))
    c = a - b
    print("Результат вычитания: " + str(a) + " - " + str(b) + " = " + str(c))
elif func == "*":
    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))
    c = a * b
    print("Результат умножения: " + str(a) + " * " + str(b) + " = " + str(c))
elif func == "/":
    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))
    c = a / b
    print("Результат деления: " + str(a) + " / " + str(b) + " = " + str(c))
elif func == "^":
    a = float(input("Введи число: "))
    b = int(input("Введи степень: "))
    c = a ** b
    print("Результат возведения в степень: " + str(a) + " ^ " + str(b) + " = " + str(c))
elif func == "sqrt()":
    a = float(input("Введи первое число: "))
    c = math.sqrt(a)
    print("Результат: sqrt(" + str(a) + ") = " + str(c))
elif func == ("Пи"):
    print("Чило Пи: " + math.pi)
else:
    print("Неподдерживаемая ф-ция!!!:(")
