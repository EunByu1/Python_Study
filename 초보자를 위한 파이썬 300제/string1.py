# 문자열 인덱싱
letters = 'python'

print(letters[0], letters[2])


# 첫 문자 대문자 만들기 
# 방법1
letters_p = letters.replace("p","P")
print(letters_p)

# 방법2
letters_P = letters.title()
print(letters_P)
# title은 문자열 객체 메소드로, 첫 글자를 대문자로 바꿔주는 기능을 가짐