from sys import stdin

count_of_coins = [0]*4
t = int(stdin.readline().strip())
for _ in range(t):
    c = int(stdin.readline().strip())

    count_of_coins[0] = c // 25
    c = c % 25

    count_of_coins[1] = c // 10
    c = c % 10

    count_of_coins[2] = c // 5
    c = c % 5

    count_of_coins[3] = c
    for count_of_coin in count_of_coins:
        print(count_of_coin, end =" ")
    print()

