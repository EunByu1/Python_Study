import datetime

present = datetime.datetime.now()

if present.minute == 00:
    print("현재시간:%d:%d" % (present.hour, present.minute))
    print("정각입니다.")
else:
    print("현재시간:%d:%d" % (present.hour, present.minute))
    print("정각이 아닙니다.")