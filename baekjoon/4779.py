def make_cantor_set(start,end):
    global cantor_set
   
    length = end - start + 1

    if start == end: 
        cantor_set[start] = "-"
        return
    make_cantor_set(start,start+ length//3 - 1)
    make_cantor_set(start + (2*length)//3,start + length - 1)

while True:
    try:
        n = int(input()) 
        cantor_set = [" "]*(3**n + 1)
        make_cantor_set(1,3**n)
        print("".join(cantor_set[1:]))
    except:
       break

