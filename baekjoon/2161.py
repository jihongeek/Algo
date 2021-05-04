from sys import stdin

cards = [x for x in range(1,int(stdin.readline().strip())+1)]
while len(cards) > 1:
    print(cards[0],end=" ")
    cards = cards[1:]
    cards.append(cards[0])
    cards = cards[1:]
print(cards[0])