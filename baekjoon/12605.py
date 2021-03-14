testcase = int(input())

for i in range(1,testcase+1):
    input_str = input().split()
    input_str.reverse()
    print(f"Case #{i}: " + " ".join(input_str))

