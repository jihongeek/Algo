from sys import stdin
"""
    전략 : 끝나는 시간이 작는 순서대로 회의시간 배정
"""
number_of_meeting = int(stdin.readline().strip())
meeting_times = []
for _ in range(number_of_meeting):
    start,end = map(int,stdin.readline().strip().split())
    meeting_time = (start,end)
    meeting_times.append(meeting_time)
meeting_times.sort(key=lambda x : (x[1],x[0]))
count = 0
now_end = -1 

for meeting_time in meeting_times:
    if now_end <= meeting_time[0]:
        count += 1
        now_end = meeting_time[1]
print(count)