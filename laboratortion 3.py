# Балахничёва Мария ИСУ 367852
from itertools import *

size = {"в": 3,"п": 2,"б": 2,"а": 2,"и": 1,"н": 1,"т": 3,"о": 1,"ф": 1,"д": 1,"к": 2,"р": 2}
points = {"в": 25,"п": 15,"б": 15,"а": 20,"и": 5,"н": 15,"т": 20,"о": 25,"ф": 15,"д": 10,"к": 20,"р": 20}
profit = []

for i in "впбаинтофдкр":      # считаем для каждого премета его "выгоду" - отношение количества очков к количеству места, которое он занимает
    profit_i = points[i]//size[i]
    profit.append([profit_i, i])

profit.sort(reverse=True)
rukzak = []                   # заведем список, в который юудем добавлять выбранные нами предметы
rukzak.append("и")            # автомаически кладём ингалятор, тк Том астматик
survive_points = 10           # заводим переменную, в которой будем считать очки выживания Тома

for i in range(12):           # кладем в рюкзак вещи в порядке их выгодности пока в рюкзаке есть место
    if (len(rukzak) + size[profit[i][1]])<=9:
        for j in range(size[profit[i][1]]):
            rukzak.append(profit[i][1])
for i in "впбаинтофдкр":      # считаем очки выживания, которые получит Том, если возьмет выбранные нами предметы
    if i in rukzak:
        survive_points += points[i]
    else:
        survive_points -= points[i]

print(rukzak[0:3])
print(rukzak[3:6])
print(rukzak[6:10])
print("Итоговое количество очков выживания для рюкзака размером 9: ", survive_points)


# допзадание 2


def max_quantity(s):                 # считаем максимальное количество предметов, которое может взять Том
    sizes = []
    for k in "впбаинтофдкр":
        sizes.append(size[k])
    sizes.sort()
    i = 0
    cnt = 0
    while s > 0:
        s -= sizes[i]
        i += 1
        cnt += 1
    return (cnt)


def min_quantity(s):                # считаем минимальное количество предметов, которое может взять Том
    sizes = []
    for k in "впбаинтофдкр":
        sizes.append(size[k])
    sizes.sort(reverse=True)
    i = 0
    cnt = 0
    while s > 0:
        s -= sizes[i]
        i += 1
        cnt += 1
    return (cnt)


def potential_comb(s):             # найдем все потенциалье комбинации предметов, которые может взять Том
    minq = min_quantity(s)
    maxq = max_quantity(s)
    potential_comb = []
    for i in range(minq - 1, maxq):
        ch = i
        bebe = list(combinations("впбантофдк", ch))
        for k in bebe:
            stroka = 'и'           # ингалятор во всех этих комбиациях есть по дефолту, кладем его отдельно; приводим комбинацию к формату строки, чтобы впоследствии с ней было удобнее работать
            for b in range(i):
                stroka += k[b]
            potential_comb.append(stroka)
    return potential_comb


def combinatsii(s):                 # проверям все потенциальные комбинации, если количесво очков выживания в них больше 0, добавляем комбинацию в ответ
    podoshlo = []
    potential_combination = potential_comb(s)
    for c in range(len(potential_combination)):
        tek_comb = potential_combination[c]
        tek_SurvPoints = 10 + 5
        for h in "впбантофдкр":
            if h in tek_comb:
                tek_SurvPoints += points[h]
            else:
                tek_SurvPoints -= points[h]
        if tek_SurvPoints > 0:
            podoshlo.append(tek_comb)
    return podoshlo

print("Все комбинации удовлетворяющие условию: ", *combinatsii(9))


# допзадание 1

if len(combinatsii(7)) != 0:        # проверяем, существуют ли комбинации для рюкзака размером 7, если да-находим самую выгодную, если нет-собщаем об  этьом
    profit = []
    for f in "впбаинтофдкр":
        profit_f = points[f] // size[f]
        profit.append([profit_f,f])
    profit.sort(reverse=True)
    rukzak = []
    rukzak.append("и")
    survive_points = 10
    for i in range(12):
        if (len(rukzak) + size[profit[i][1]]) <= 7:
            for j in range(size[profit[i][1]]):
                rukzak.append(profit[i][1])
    for i in "впбаинтофдкр":
        if i in rukzak:
            survive_points += points[i]
        else:
            survive_points -= points[i]
    print(rukzak)
    print("Итоговое количество очков выживания для рюкзака размером 7: ", survive_points )
else:
    print("Решений для рюкзака размером 7 нет")