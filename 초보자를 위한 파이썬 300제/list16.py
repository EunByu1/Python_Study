interest = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]

# 방법 1
print("{} {} {} {} {}".format(interest[0], interest[1], interest[2], interest[3], interest[4]))

# 방법 2
print(" ".join(interest))

# LAB
print("!!".join(interest))

# "요소 사이, 사이에 넣고 싶은 문자열".join(리스트명)
# 리스트 안에 각각의 요소들을 해당 문자열로 연결해서 문자열 형태로 출력