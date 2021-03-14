n = int(input())
cards = []

for i in range(1,n+1):
    cards.insert(0, i)
for i in range(n):
    cards.pop()
    if len(cards) == 1:
        print(cards[0])
        break
    num = cards.pop()
    cards.insert(0,num)