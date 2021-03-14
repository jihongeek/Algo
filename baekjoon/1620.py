import sys
from string import ascii_uppercase

alphabets = ascii_uppercase
dogam_nums = {}
dogam_strs = {}
inputstr = sys.stdin.readline().strip().split()
dogam_num = inputstr[0]
display_num = inputstr[1]

for i in range(int(dogam_num)):
    dogam_nums[i] = sys.stdin.readline().strip()
    dogam_strs[dogam_nums[i]] = i

for i in range(int(display_num)):
    command = sys.stdin.readline().strip()
    if command[0] in alphabets:
        print(dogam_strs[command]+1)
    else:
        print(dogam_nums[int(command)-1])
    

