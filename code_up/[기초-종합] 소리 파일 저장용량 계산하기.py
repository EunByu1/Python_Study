value_1, value_2, value_3, value_4 = map(int, input().split())
result = (value_1*value_2*value_3*value_4) / 8 / 1024 / 1024
print("%.1f MB" % result)
