num_arr = []

for i in range(19):
    num_arr.append([])
    for j in range(19):
        num_arr[i].append(0)

# 입력: n개의 흰 돌
value = int(input())
for i in range(value):
    row, col = map(int, input().split())
    num_arr[row-1][col-1] = 1

for i in range(19):
    for j in range(19):
        print(num_arr[i][j], end=" ")
    print()
