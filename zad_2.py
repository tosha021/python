#2
user_var = int(input("Введите время в секундах: "))
hours = user_var//3600
minutes = (user_var%3600) // 60
seconds = (user_var%3600) % 60

print(f'{hours}:{minutes}:{seconds}')