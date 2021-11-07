# 방법 1
user  = input("입력: ").split(" ")
money = int(user[0])
unit  = user[1]

if unit == "달러":
    daller = float(money * 1167)
    print("%.2f 원" % daller)
elif unit == "엔":
    en = float(money) * 1.096
    print("%.2f 원" % en)
elif unit == "유로":
    uro = float(money * 1298)
    print("%.2f 원" % uro)
else:
    Yuan = float(money * 171)
    print("%.2f 원" % Yuan)

# 방법 2
환율 = {
    "달러" : 1167,
    "엔"   : 1.096,
    "유로" : 1268,
    "위안" : 171
}

money, unit = input("입력: ").split(" ")
print(float(money) * 환율[unit], "원")