from sys import stdin
n = int(stdin.readline().strip()) 
cases = [0] * (n+1)
cases[0] = 1
cases[1] = 2
for i in range(2,n):
    cases[i] = (cases[i-1] % 10007 + cases[i-2] % 10007) % 10007
print(cases[n-1])