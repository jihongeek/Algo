testcase = int(input())

while(testcase):
    testcase = testcase - 1
    credit_sum = 0
    credit_num = list(map(int,input()))

    for i in range(-1,-len(credit_num)-1,-1):
        if i % 2 == 0:
            if credit_num[i] * 2 >= 10:
                credit_num[i] = credit_num[i] * 2
                credit_num[i] = 1 + (credit_num[i] % 10)
            else:
                credit_num[i] = credit_num[i]*2
    credit_sum = sum(credit_num)
    if credit_sum % 10 == 0:
        print("T")
    else:
        print("F")

