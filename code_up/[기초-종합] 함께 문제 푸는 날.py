p_1, p_2, p_3 = map(int, input().split())
count = 1

while(1):
  if((count % p_1 == 0) & (count % p_2 == 0) & (count % p_3 == 0)):
    print(count)
    break

  count = count + 1
