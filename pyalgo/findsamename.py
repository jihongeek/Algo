#나의 코드
names = ['kane','kane']
n_names=set()
same_name = set()
for i in range(0,len(names)):
	if names[i] in n_names:
		same_name.add(names[i])
	else:
		n_names.add(names[i])
print(same_name)
#집합으로 풀기(책의 코드)
def fine_same_name(a):
	n = len(a)
	result = set()
	for  i in range(0,n-1):
		for j in range(i+1,n):
			if a[i] == a[j]:
				result.add(a[i])
	return result
print(fine_same_name(names))