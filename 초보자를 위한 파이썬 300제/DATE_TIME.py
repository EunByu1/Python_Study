import datetime

present = datetime.datetime.now()

print(f"{present.year}년")
print("%d월" % present.month)
print("{}일".format(present.day))
print(f"{present.hour}시")
print("%d분" % present.minute)
print("{}".format(present.second))