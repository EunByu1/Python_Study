user = input("주민등록번호: ").split("-")[1]

if user.startswith(("1", "3")):
# 값이 2개 이상이면, 제발 괄호로 묶어!!!!
    print("남자")
else:
    print("여자")