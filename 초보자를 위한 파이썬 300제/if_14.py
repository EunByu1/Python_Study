phone_num = input("휴대전화 번호 입력: ").split("-")[0]
# phone_num = phone_num[0]
if phone_num == "011":
    print("당신은 SKT 사용자입니다.")
elif phone_num == "016":
    print("당신은 KT 사용자입니다.")
elif phone_num == "019":
    print("당신은 LGU 사용자입니다.")
else:
    print("알수없음")