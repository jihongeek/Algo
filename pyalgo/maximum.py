#리스트에서 최댓값 구하기
nums=[67,65,98,55,0]
max=nums[0]
for i in range(1,len(nums)):
	if max < nums[i]:
		max = nums[i]
print(max)
#리스트에서 최솟값 구하기
min = nums[0]
for i in range(1,len(nums)):
	if min > nums[i]:
		min = nums[i]
print(min)