phone_number = "010-1111-22223"

# 방법 1
print(phone_number[:3], phone_number[4:8], phone_number[-4:])

# 방법 2
phone_numbr1 = phone_number.replace("-"," ")
print(phone_numbr1)

# lab
phone_numbr2 = phone_number.replace("1","")
print(phone_numbr2)

# 문자열에서 repalce 메서드를 사용하면, 기존문자를(들을) 새로운 문자로 바꿀 수 있음.