from sys import stdin 

charge = 1000 - int(stdin.readline().strip())
print(charge // 500 + charge%500//100 +  charge%100//50 + charge%50//10 + charge%10//5+charge%5//1)