T = int(input())

for i in range(T):
    n = int(input())
    case = list(map(int, input().split()))
    result = 0

    while case:
        M = case.index(max(case))  # 현 구간의 max 인덱스

        result -= sum(case[:M])
        result += M * case[M]

        del case[:M + 1]

    print(f"#{i+1} {result}")
