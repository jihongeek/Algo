inputlist = input().split()
ascending = ["1","2","3","4","5","6","7","8"]
descending = list(reversed(ascending))
if inputlist == ascending:
    print("ascending",end="")
elif inputlist == descending:
    
    print("descending",end="")
else:
    print("mixed",end="")
    
    