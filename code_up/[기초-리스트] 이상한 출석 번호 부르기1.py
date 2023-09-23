n = int(input())
tmp_list = list(map(int, input().split()))
num_list = []

for i in range(23):
  num_list.append(0)

for i in tmp_list:
  i = i - 1
  num_list[i] = num_list[i] + 1

for i in range(23):
  print(num_list[i], end=" ")
