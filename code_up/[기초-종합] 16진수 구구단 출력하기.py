value_16 = input()
value_10 = int(value_16, 16)

for i in range(1, 15+1):
  print("%s*%X=%X" % (value_16, i, (value_10 * int(i))))
