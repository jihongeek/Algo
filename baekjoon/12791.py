albumdict = {}
albums = """1967 DavidBowie
1969 SpaceOddity
1970 TheManWhoSoldTheWorld
1971 HunkyDory
1972 TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars
1973 AladdinSane
1973 PinUps
1974 DiamondDogs
1975 YoungAmericans
1976 StationToStation
1977 Low
1977 Heroes
1979 Lodger
1980 ScaryMonstersAndSuperCreeps
1983 LetsDance
1984 Tonight
1987 NeverLetMeDown
1993 BlackTieWhiteNoise
1995 1.Outside
1997 Earthling
1999 Hours
2002 Heathen
2003 Reality
2013 TheNextDay
2016 BlackStar""".split("\n")
for i in albums:
    year = int(i[:4])
    name = i[5:]
    if year in albumdict:
        albumdict[year].append(name)
    else:
        albumdict[year] = [name]
q = int(input())
for i in range(0,q):
    query = input().split()
    start = int(query[0])
    end = int(query[1])
    sumall =0
    albumdisplay = []
    for j in range(start,end+1):
        if j in albumdict:
            sumall += len(albumdict[j])
            for k in albumdict[j]:
                albumdisplay.append((j,k))
    print(sumall)
    for j in albumdisplay:
        print("%d %s"%(j[0],j[1]))