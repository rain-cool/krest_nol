tabl = [[' ', '0', '1', '2'],
        ['0', '-', '-', '-'],
        ['1', '-', '-', '-'],
        ['2', '-', '-', '-']]

znach = []
count = 1
tabl_s = '\n'.join([' '.join(map(str, row)) for row in tabl])
print(tabl_s)


def srav_diag(x):
    global count
    if x[1][1] == x[2][2] and x[2][2] == x[3][3]:
        if x[1][1] == 'x':
            count += 10
            return 'x winner'
        elif x[1][1] == '0':
            count += 10
            return '0 winner'
        else:
            return 'NEXT ROUND'
    elif x[1][3] == x[2][2] and x[2][2] == x[3][1]:
        if x[1][3] == 'x':
            count += 10
            return 'Крестик выйграл'
        elif x[1][3] == '0':
            count += 10
            return 'Нолик выйграл'
        else:
            return 'NEXT ROUND'
    else:
        return 'good'


while count < 10:
    if count % 2 != 0:
        print('Ставим крестик')
    else:
        print('Ставим нолик')
    h = int(input('Выберите номер горизонтали:'))
    v = int(input('Выберите номер вертикали:'))
    if tabl[h + 1][v + 1] == '-':
        if count % 2 != 0:
            tabl[h + 1][v + 1] = 'x'
        else:
            tabl[h + 1][v + 1] = '0'
        count += 1
    else:
        print('Место занято')
    tabl_s = '\n'.join([' '.join(map(str, row)) for row in tabl])
    print(tabl_s)
    for i in tabl:
        znach.append(i[v + 1])
        if znach[1:] == ['x', 'x', 'x']:
            print('Крестик выйграл')
            count += 10
        elif znach[1:] == ['0', '0', '0']:
            print('Нолик выйграл')
            count += 10
    if tabl[h + 1][1:] == ['x', 'x', 'x']:
        print('Крестик выйграл')
        count += 10
    elif tabl[h + 1][1:] == ['0', '0', '0']:
        print('Нолик выйграл')
        count += 10
    znach = []
    print(srav_diag(tabl))

print('FINISH')