import math
while True: #цикл обработки ввода количества критериев
    try:
        lot = int(input('\nВведите количество критериев (целое число большее 1): '))
        assert lot > 1 
        break
    except ValueError:
        print('некорректный ввод\nповторите попытку ввода')
    except AssertionError:
        print('некорректный ввод\nповторите попытку ввода')

#cоздание таблицы попарного сравнения состоящей из единиц
table = [[1.0] * lot for i in range(lot)]

#цикл обработки заполнения таблицы
while True:
    try: 
        for i in range(lot - 1):
            for j in range(i + 1, lot):
                table[i][j] = float(input(f'Насколько параметр {i+1} важнее параметра {j+1}: '))
                table[j][i] = 1 / table[i][j]
                #oкругление до двух знаков после запятой(или до 0, если число больше 1)
                if table[i][j] > 1:
                    table[i][j] = float(math.floor(table[i][j]))
                else:
                    table[i][j] = float(math.floor(table[i][j] * 100)/100)
                if table[j][i] > 1:
                    table[j][i] = float(math.floor(table[j][i]))
                else:
                    table[j][i] = float(math.floor(table[j][i] * 100)/100)
        break
    except ValueError:
        print('некорректный ввод\nповторите попытку ввода')
    except ZeroDivisionError:
        print('некорректный ввод\nповторите попытку ввода')

#создание и заполнение списка сумм столбцов
sum_column = []

for j in range(lot):
    s = 0
    for i in range(lot):
        s += table[i][j]
        sum_column.append(s)

#создание и заполнение списка весовых коэффициентов
list_coeff = []

for i in range(lot):
    list_coeff.append(math.floor((sum_column[i] / sum(sum_column)) * 100) / 100)

#сумма весовых коэффициентов и ее округление до двух знаков
listsum = round(sum(list_coeff), 2)

#доведение суммы до 1
while listsum > 1:
    for i in range(lot):
        if list_coeff[i] == min(list_coeff):
            list_coeff[i] -= 0.01
        listsum = round(sum(list_coeff), 2)
while listsum < 1:
    for i in range(lot):
        if list_coeff[i] == max(list_coeff):
            list_coeff[i] += 0.01
    listsum = round(sum(list_coeff), 2)

# Вывод таблицы
print('\nТаблица попарного сравнения')
for i in range(lot):
    for j in range(lot):
        print(table[i][j], end=' \t')
    print('')

# Вывод коэффициентов
print('\nКоэффициенты')
for i in range(lot):
    print(f'Коэффициент критерия {i+1}: {round(list_coeff[i], 2)}')
