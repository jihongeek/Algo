num = input()
seats = input()
origin = seats
count = 0
while 1:
    if "S" not in seats and "LL"  not in seats:
        break
    if "S" in seats:
        seats = seats.replace("S","O",1)
        count += 1
    elif "LL" in seats:
        seats = seats.replace("LL","O",1)
        count += 1
if (len(origin) < count+1):
    print(len(origin))
else:
    print(count+1)


    
        