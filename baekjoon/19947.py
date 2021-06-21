from sys import stdin
def maxMoney(year, money):
    if year == 0:
        return money
    maxOfMoney = 0
    if year - 1 >= 0:
        maxOfMoney = max(maxOfMoney,maxMoney(year-1,int(money*1.05)))
    if year - 3 >= 0:
        maxOfMoney = max(maxOfMoney,maxMoney(year-3,int(money*1.2)))
    if year - 5 >= 0:
        maxOfMoney = max(maxOfMoney,maxMoney(year-5,int(money*1.35)))
    return maxOfMoney

h,y = map(int,stdin.readline().strip().split())
print(maxMoney(y,h))

