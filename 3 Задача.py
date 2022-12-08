import math
print("Введите коэффициент a: ")
a = float(input())
print("Введите коэффициент b: ")
b = float(input())
print("Введите коэффициент c: ")
c = float(input())
disk = (b ** 2) - 4 * (a * c)
if disk > 0:
    x1 = (-b + math.sqrt(disk)) / (2 * a)
    x2 = (-b - math.sqrt(disk)) / (2 * a)
    print(f"Ответ: {x1, x2}")
elif disk == 0:
    print(f"Ответ: {-b/2*a}")
else:
    print("Корней нет")