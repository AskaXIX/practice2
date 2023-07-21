# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

n = int(input("n: "))
coins = []

for i in range(n):
    coins.append(randint(0, 1))
print(coins)

coins_0 = coins.count(0)
coins_1 = coins.count(1)

if coins_0 > coins_1:
    print(f"\n{coins_1}")
else:
    print(f"\n{coins_0}")
