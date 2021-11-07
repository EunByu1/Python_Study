data = [2, 4, 3, 1, 5, 10, 9]

# 방법1
D1 = [data[3], data[0], data[2], data[1], data[4], data[6], data[5]]
print(D1)

# 방법2
D2 = sorted(data)
print(D2)

# 방법3
data.sort()
print(data)

#-------------------------------------------역으로
D2.reverse()
print(D2)