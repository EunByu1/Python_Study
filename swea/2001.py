T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr  = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    cnt = 0
    
	# move
    for si in range(N-M+1):
        for sj in range(N-M+1):
            cnt = 0
            # slicing
            for i in range(si, si+M):
                for j in range(sj, sj+M):
                    cnt += arr[i][j]
                    
            if ans < cnt:
                ans = cnt
                
    print(f"#{test_case}", ans)
                
