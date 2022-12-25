# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
xyz = ["X", "Y", "Z"]
pred = [3]
for i in range(3):
    pred.append(input(f"Введите значение {xyz[i]}: "))

leftSt = not (pred[0] or pred[1] or pred[2])
rightSt = not pred[0] and not pred[1] and not pred[2]
#print(leftSt)
#print(rightSt)
if leftSt == rightSt:
    print("Утверждение верно")
else:
    print(f"Утверждение ложно")