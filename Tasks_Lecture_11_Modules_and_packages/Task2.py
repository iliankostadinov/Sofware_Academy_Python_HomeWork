# Задача 2. Създайте модул под името “calculation.py”, който да има само една
# функция вътре в него. Тази функция трябва да пресмята лице на правоъгълник.
# Програмата трябва да има две променливи length и width. Функцията да се казва
# calc_area(length, width).

import calculation

rect_lenght = input("Please enter rectangle length: ")
rect_width = input("Please enter rectangle width: ")

area = calculation.calc_area(rect_lenght, rect_width)
print(f"Rectangle area is {area}")

