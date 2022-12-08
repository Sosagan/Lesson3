c = input("Введите координаты u-вверх, d-вниз, l-влево, r-вправо: ")
X, Y = 0, 0
for i in c:
    if i == "u":
        Y += 1
    elif i == "d":
        Y -= 1
    elif i == "r":
        X += 1
    elif i == "l":
        X -= 1
print(X, Y)


