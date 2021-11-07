# 문자가 숫자로만 이루어져 있는지 확인해줌
print('abc'.isnumeric())
print('132'.isnumeric())


# 문자를 숫자로 표현할 수 있음(아스키 코드 10진법으로 표현함)
print("a :", ord('a'))

# 숫자를 문자로 표현할 수 
print(ord('a'),":",chr(ord('a')))