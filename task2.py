# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек


cities = ['Суздаль', 'Саранск', 'Бобруйск', 'Крыжополь']

population =[
    [cities[0], 9597],
    [cities[1], 314871],
    [cities[2], 212200],
    [cities[3], 9011]
]

print('Население Саранска - ', population[1][1], 'человек')

x = sum(population, [])

total_population = x[1] + x[3] + x[5] + x[7]
print('Итого размер населения - ', (total_population), 'человек')
