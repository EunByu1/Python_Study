print("해당 종목이 투자 경고 종목인지 확인해 드리겠습니다.")

user = input("입력하세요: ")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

if user in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")