value  = int(input())
tmp    = 1
count  = 2
result = 1

while (1):
  if(tmp == value):
    break
  if(value <= result):
    break
  result = result + count
  count  = count + 1
  
print(result)
