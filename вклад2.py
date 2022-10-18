v=int(input("Введите сумму вклада:"))
deposit = []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

t=per_cent.get('ТКБ')# достаю из словаря значение
tkb=v*t/100# считаю процент за год

t2=per_cent.get('СКБ')
skb=v*t2/100

t3=per_cent.get('ВТБ')
vtb=v*t3/100

t4=per_cent.get('СБЕР')
sber=v*t4/100

deposit.append(int(tkb))# добавляю в список и преобразую в целое число  
deposit.append(int(skb))
deposit.append(int(vtb))
deposit.append(int(sber))

print("Вклады", deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
