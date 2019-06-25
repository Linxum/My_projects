i = 1

for i in range(3):
	function = input("Функция: ")
	a = float(input("Введите первое число: "))
	b = float(input("Введите второе число: "))
		
	if function == "+":
		c = a + b
		print("Результат сложения: " + str(c))
	elif function == "-":
		c = a - b
		print("Результат вычитания: " + str(c))
	elif function == "*":
		c = a * b
		print("Результат умножения: " + str(c))
	elif function == "/":
		c = a / b
		print("Результат деления: " + str(c))
	elif function == "%":
		c = a / b * 100
		print("Результат в процентах: " + str(c) + "%")
	else:
		print("Недопустимая фукция!!! =(")