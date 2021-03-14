input_str = input()
length_half = int(len(input_str)/2)

first = list(input_str[:length_half])
second = list(input_str[length_half:])

mapped_first = map(int,first)
mapped_second = map(int,second)

if sum(mapped_first) == sum(mapped_second):
    print("LUCKY")
else:
    print("READY")