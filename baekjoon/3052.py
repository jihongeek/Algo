namojilist = []
for i in range(10):
    namojilist.append(int(input())%42)
for i in namojilist:
    if namojilist.index(i)+1 == len(namojilist):
        pass
    elif i in namojilist[namojilist.index(i)+1:]:
       namojilist.remove(i) 
print(len(namojilist),end="")
