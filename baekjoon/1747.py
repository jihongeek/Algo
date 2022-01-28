from sys import stdin 
"""
    전략:
    1. 에라토스테네스의 체를 이용하여 n 까지의 소수를 구한다.
    2. n 이상의 팰린드롬 수를 찾는다.
    3. 2.에서 찾은 팰린드롬 수가 소수인지 root(n)까지 나누어서 확인 해본다.


    팰린드롬을 어떻게 확인할까?
    -> 팰린드롬은 중앙 인덱스를 기준으로 하여 좌우가 대칭이다.
    -> 현재인덱스와 마지막인덱스 - 현재 인덱스의 내용이 같아야 된다.
    -> 전체 문자열에 대해 모두 진행할 필요없이 절반 정도만 진행해도 알 수 있다. 
    -> 문자열길이/2 - 1 만큼만 확인 하면 된다.
    
    에라토스테네스체는 루트(n)의 배수만 지워도 상관없다. 
    -> 배수는 합성수인데 합성수를 두 약수의 곱으로 나타냈을 때 무조건 root(그 수)이하의 약수를 적어도 하나를 갖기 때문이다.
"""
def isPalindrome(num_str):
    length = len(num_str)
    for i in range(length//2):
        if num_str[i] != num_str[length-1-i]:
            return False
    return True 

n = int(stdin.readline().strip())
sieve = [True]*1000001  

for number in range(2,1001):
    if not sieve[number]:
        continue
    for divisor in range(number+number,1000001,number):
        sieve[divisor] = False

primes = []
for i in range(2,1000001):
    if sieve[i]:
        primes.append(i)

number = n 
while True:
    isPrime = True 
    if not isPalindrome(str(number)) or number == 1:
        number += 1
        continue
    if number < 1000000 and sieve[number]: 
        break
    for prime in primes:
        if prime * prime > number:
            break
        if  number % prime == 0:
            isPrime = False
            break 
    if isPrime:
        break
    number += 1
print(number)




