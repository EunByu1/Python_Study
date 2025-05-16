T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N)]
    ans = "1" 
    
    if N == 1:
        print(f"#{test_case}")
        print(ans)
    else:
        print(f"#{test_case}")
        print(ans)
        for i in range(1, N):
            ans = "1"
            for j in range(1, N):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
                ans = ans + " " + str(arr[i][j])
            ans = ans.rstrip(" 0 ")
            print(ans)
           
        
