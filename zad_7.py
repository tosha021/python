#7
a = int(input('Введите к-во км пробежки в первый день: '))
b = int(input('Введите требуемый результат в км: '))
c = 0
count = 0
while a <= b:
    count += 1
    a = a + c
    c = (a/100)*10
    x = round(a, 2)
    print(f'{count}-й день:{x}')