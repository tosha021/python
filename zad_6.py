# 6
revenue = int(input("Введите выручку: "))
cost = int(input("Введите издержку: "))
if revenue > cost:
    profit = revenue - cost
    print("Фирма получила прибыль: ", profit)
    profitability = profit / revenue
    print('Рентабльность выручки: ', profitability)
    workers = int(input("Введите количество сотрудников фирмы: "))
    ppu = profit / workers
    print("Прибыль фирмы в расчете на одного сотрудника", ppu)

elif revenue < cost:
    loss = cost - revenue
    print("Фирма понесла убытки")
else:
    print("Фирма вышла в 0")