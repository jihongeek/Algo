#반복문을 쓰지 않고 합 구하기
n=10
num = list(range(1,n+1))
print(sum(num))
#일반적인 방법
n = 10
sum =0
for i in range(1,n+1):
	sum= sum+i
print(sum)
#시그마 공식(n*(n+1)/2)
n= 10
print(int(n*(n+1)/2))
#n**2 버전
n = 10
sum =0
for i in range(1,n+1):
	sum= sum +i**2
print(sum)
# 시그마공식(k**2)
n =10
print(int(n*(n+1)*(2*n+1)/6))