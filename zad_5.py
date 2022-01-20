# 5
revenue = int(input("Введите выручку: "))
cost = int(input("Введите издержку: "))
if revenue > cost:
    profit = revenue - cost
    print("Фирма получила прибыль: ", profit)
elif revenue < cost:
    loss = cost - revenue
    print("Фирма понесла убытки")
else:
    print("Фирма вышла в 0")