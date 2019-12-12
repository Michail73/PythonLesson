from math import log, ceil

k = input('Введите k от 0 до 9: ')

if not k.isdigit() or int(k) < 0 or int(k) > 9:
    print('Неверный ввод!')
    raise SystemExit

if k == '0':
    print('0')
    raise SystemExit

k = int(k)

a = 1  # A начальное
for p in range(200):
    i = ceil(log(a + 0.5, 10))  # количество разрядов в А
    flag = False  # для завершения основного цикла
    while True:
        n = 10 * a + k

        part1 = k * n  # левая часть равенства
        part2 = a + k * 10 ** i  # правая часть равенства

        if part1 > part2:
            if p >= 8:
                a = 1000 * (a // 1000) * 10  # гениальная строчка
            else:
                a = 10 ** p
            break
        elif part1 == part2:
            print(f'n={a}{k}')
            flag = True
            break

        a += 1

    if flag:
        break

