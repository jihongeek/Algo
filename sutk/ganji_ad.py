gan = ['기','무','정','병','을','갑','계','임','신','경']
ji = ['자','축','인','묘','진','사','오','미','신','유','술','해']
ji.reverse()
this_year = "정인년"
pair = (gan.index(this_year[0]),ji.index(this_year[1]))
d =abs(2019 - int(1919))
print(gan[d%10]+ji[d%12]+"년")
gan_nums =[]
ji_nums =[]
for i in range(0,10):
	gan_nums.append(10*i+pair[0])
	ji_nums.append(12*i+pair[1])
for i in gan_nums:
	if i in ji_nums:
		print(2019-i)
