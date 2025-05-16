T = int(input())

for test_case in range(1, T+1):
    N   = int(input())
    arr = [[0] * N for _ in range(N)]
    
    di = [0, 1, 0, -1] 	# 상하로 이동
    dj = [1, 0, -1, 0] 	# 좌우로 이동 
    
    i, j, cnt, dr = 0, 0, 1, 0
    arr[i][j] = cnt
    cnt += 1
    
    while cnt <= N * N:
        ni = i +di[dr]
        nj = j+dj[dr]
        if (0<=ni<N) and (0<=nj<N) and (arr[ni][nj] == 0):
            i = ni
            j = nj
            arr[i][j] = cnt 
            cnt += 1
        else:
            dr = (dr+1) % 4
         
    print(f"#{test_case}")
    for val in arr: 
        print(*val)
