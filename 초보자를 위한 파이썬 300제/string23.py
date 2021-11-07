a = "hello"

# 방법1
print(a.title())

# 방법2
a1 = a.replace("h","H")
print(a1)

# 방법3
a2 = a.capitalize()
print(a2)

# LAB
b = "hello, bro"
b1 = b.title()
b2 = b.capitalize()

print(b)
print(b1)
print(b2)

# .title() 메서드는 공백 기준으로 알파벳 첫글자를 '모두' 대문자로 바꿈
# .capitalize() 메서드는 앞에 나온 알파벳 첫글자'만' 대문자로 바꿈