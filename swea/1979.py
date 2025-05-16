T = int(input())

for test_case in range(1, T+1):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)] 
    check = [1] * N
    ans = 0 
    
    for _ in range(2):  # 가로 + 세로
        for i in range(M):
            for j in range(M - N + 1):
                if arr[i][j:j+N] == check:
                    left_ok = (j == 0) or (arr[i][j - 1] == 0)
                    right_ok = (j + N == M) or (arr[i][j + N] == 0)
                    if left_ok and right_ok:
                        ans += 1
        arr = [list(x) for x in zip(*arr)]  # 전치

    print(f"#{test_case} {ans}")
