name = ""
count = 0

while name != "Левон":
    name = input("Введите имя: ")
    count += 1
    if name == "Александра":
        num1 = count
    elif name == "Левон":
        num2 = count
print(f"Между Александрой и Левоном: {num2 - num1 - 1}")
