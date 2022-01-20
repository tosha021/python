# 4
var = str(input("Введите целое положительное число: "))
a = var[0]
i = 0
while i != (len(var)):
    if a <= var[i]:
        a = var[i]
    i += 1

print(a)