price = int(input("Введите цену услуги: "))
coin1 = 0
coin5 = 0
coin10 = 0
coin25 = 0

while price > 0:
    if price - 25 > 0:
        price -= 25
        coin25 += 1
    elif price - 10 > 0:
        price -= 5
        coin10 += 1
    elif price - 5 > 0:
        price -= 10
        coin5 += 1
    else:
        price -= 1
        coin1 += 1

print(f"""Столько монет вы должны заплатить Ведьмаку:

| Всего: {coin1 + coin5 + coin10 + coin25} монет(-а, -ы)

| {coin1} монет по 1
| {coin5} монет по 5
| {coin10} монет по 10
| {coin25} монет по 25

""")
