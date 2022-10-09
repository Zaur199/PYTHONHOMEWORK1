# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 

def SomeNumbers(j): # Решим с введением функции
    xyz = ["X", "Y", "Z"]
    lst = []
    for i in range(j):
        lst.append(input(f"Введите значение {xyz[i]}: "))
    return lst


def Predicates(j): # Опишем левую и правые части и сравним их
    left_side = not (j[0] or j[1] or j[2])
    right_side = not j[0] and not j[1] and not j[2]
    result = left_side == right_side
    return result


confirmation = SomeNumbers(3) # Так как у нас 3(x,y,z) переменные, то в функцию подставим цифру 3

if Predicates(confirmation) == True:
    print(f"Утверждение является истинным")
else:
    print(f"Утверждение является ложным")