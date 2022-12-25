# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
import sys
def koordXY(x):
    xy = ["X", "Y"]
    a = []
    try:
        for i in range(x):
        
            a.append(int(input(f"Введите значение {xy[i]}: ")))
    except ValueError:
        print("Вы ввели не число")
        sys.exit()
    return a
print("Введите координаты точки A")
pA = koordXY(2)
print("Введите координаты точки В")
pB = koordXY(2)

result = ((pB[0] - pA[0]) ** 2 + (pB[1] - pA[1]) ** 2) ** (0.5)
print (f"Длинна отрезка = {result}")
