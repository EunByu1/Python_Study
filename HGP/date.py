import datetime

present = datetime.datetime.now()

#print(present.year, "년")
#print(present.month, "월")
#print(present.day, "일")
#print(present.hour, "시")
#print(present.minute, "분")
#print(present.second, "초")

print("{}{}".format(present.year, "년"))
print("{}{}".format(present.month, "월"))
print("{}{}".format(present.day, "일"))
print("{}{}".format(present.hour, "시"))
print("{}{}".format(present.minute, "분"))
print("{}{}".format(present.second, "초"))