url = "htttp://sharebook.kr"

# 방법1
print(url[-2:])

# 방법2
url = url.split(".")
print(url[1])

# 실험
# url = url.split("t")
# print(url)
# 결과 : ["h", "", "p://sharebook.kr"]
# t를 기준으로 문자를 나눌때, 위와 같이 기준이 연속으로 2번이상 있을 경우 ""가 리스트안에 같이 들어감
# 기준이 하나만 있으면 리스트안에 안들어가고, 2번 연속으로 있으면 ""가 1개 들어가고, 3번 연속으로 있으면 ""가 2번 들어감.
