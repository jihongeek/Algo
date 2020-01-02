subjectnum = int(input())
scorelist = input().split()
maximum = 0
for i in scorelist:
    if int(i) > maximum:
        maximum = int(i)
for i,j in enumerate(scorelist):
    scorelist[i] = int(j)/maximum*100
print(sum(scorelist)/subjectnum,end="")
