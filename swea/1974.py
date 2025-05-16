T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for i in range(9)]

    answer = 1

    # 가로 세로 줄 검사
    for i in range(9):
        x = arr[i]
        y = [j[i] for j in arr]
        if len(set(x))!=9 or len(set(y))!=9:
            answer = 0
            break

    # 정사각형 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            trial = []
            for l in range(3):
                for k in range(3):
                    trial.append(arr[i+l][j+k])
            if len(set(trial)) !=9:
                answer = 0
                break
        if answer==0:
            break

    print(f"#{test_case} {answer}")
