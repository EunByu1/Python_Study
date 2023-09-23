red, green, blue = map(int, input().split())
count = 0

for r in range(red):
  for g in range(green):
    for b in range(blue):
      count = count + 1
      print("%d %d %d" % (r, g, b))

print(count)
