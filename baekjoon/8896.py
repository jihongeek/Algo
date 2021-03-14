testcase = int(input())

for _ in range(testcase):
    count = 0
    n = int(input())
    orders = [list(input()) for i in range(n)]

    for i in range(len(orders[0])):
        location = {
            'R' : [],
            'S' : [],
            'P' : [],
            'N' : []
        }
        
        for j in range(n):
            location[orders[j][i]].append(j)
        
        # 묵찌빠인 경우이므로, 무승부, 다음게임으로 
        if len(location['R']) and len(location['S']) and len(location['P']):
            continue
        # 찌와 빠만 존재하는 경우
        elif len(location['R']) == 0 and len(location['S']) and len(location['P']):
            # 빠의 좌표값들을 가져와서 해당 로봇의 모든 게임의 값을 N으로 만들기 
            for j in location['P']:
                orders[j] = ['N']*len(orders[0])
            # 빠의 좌표 비우기
            location['P'] = []    
        
        # 찌와 묵만 존재하는 경우
        elif len(location['P']) == 0 and len(location['S']) and len(location['R']):
            # 찌의 좌표값들을 가져와서 해당 로봇의 모든 게임의 값을 N으로 만들기 
            for j in location['S']:
                orders[j] = ['N']*len(orders[0])
            # 찌의 좌표 비우기
            location['S'] = []

        # 빠와 묵만 존재하는 경우
        elif len(location['S']) == 0 and len(location['R']) and len(location['P']):
            # 묵의 좌표값들을 가져와서 해당 로봇의 모든 게임의 값을 N으로 만들기 
            for j in location['R']:
                orders[j] = ['N']*len(orders[0])
            # 묵의 좌표 비우기
            location['R'] = []    
    # 승자가 결정나지 않은 경우 
    if len(location['R']) > 1 or len(location['S']) > 1 or len(location['P']) > 1:
        print(0)
    # 묵찌빠
    elif len(location['R']) and len(location['S']) and len(location['P']):
        print(0)
    # 승자가 결정된 경우 
    else:
        for i in ['R','S','P']:
            if len(location[i]) > 0:
                print(location[i][0]+1)
                break

        
    
        
            
            
        
        

                




