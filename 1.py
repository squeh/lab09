n = int(input("Введите натурально число: "))
num = 1
while num <= n:
    if 5 <= num <= 9 or 17 <= num <= 37 or 78 <= num <= 87:
        num += 1
        continue
    print(num)
    num += 1
