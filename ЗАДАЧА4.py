# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

fourth = int(input('Введите номер четверти: '))
if (fourth == 1):
    print('x > 0 and y > 0')

if (fourth == 2):
    print('x < 0 and y > 0')

if (fourth == 3):
    print('x < 0 and y < 0')

if (fourth == 4):
    print('x > 0 and y < 0')

else: 
    print('Ошибка. Введите число от 1 до 4')
