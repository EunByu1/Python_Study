T          = int(input())
result   = 0
data_1 = []
data_3 = []

for i in range(T):
    num = int(input())
    data_1.extend(list(map(int, input().split())))
    data_2 = list(set(data_1))
    
    for j in data_2:
        data_3.append(data_1.count(j))
        
    result = data_2[data_3.index(max(data_3))]
    print(f"#{num} {result}")
    data_1 = []
    data_2 = []
    data_3 = []
