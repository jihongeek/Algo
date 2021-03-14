odd_nums = []
for i in range(7):
    input_num = int(input())
    if input_num % 2 != 0:
        odd_nums.append(input_num)
if odd_nums == []:
    print(-1)
else:
    print(sum(odd_nums))
    print(sorted(odd_nums)[0])