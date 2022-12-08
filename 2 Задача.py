X, Y = 0, 0
while True:
    с = input("Введите координату u-вверх, d-вниз, l-влево, r-вправо, stop - остановиться: ")
    if с == "up":
        Y += 1
    elif с == "down":
        Y -= 1
    elif с == "right":
        X += 1
    elif с == "left":
        X -= 1
    elif с == "stop":
        break
    print(X, Y)
