import math
import decimal

decimal.getcontext().prec = 42

PI = decimal.Decimal(math.pi)

diameter = decimal.Decimal(input('Введите диаметр круга: '))

circumference = PI * diameter
area_circle = PI * (diameter / 2) ** 2

print(f'Длина окржности = {circumference}')
print(f'Площадь круга = {area_circle}')
