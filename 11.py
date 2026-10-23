from math import sqrt
xc = float(input())
yc = float(input())
r = float(input())
x = float(input())
y = float(input())
distance = sqrt((x - xc)**2 + (y - yc)**2)
if distance < r:
    print("Точка внутри окружности")
elif distance > r:
    print("Точка вне окружности")
else:
    print("Точка лежит на окружности")