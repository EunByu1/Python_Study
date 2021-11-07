# 수학에서 말하는 정수일 경우 True를 return함 
# 수학에서 말하는 정수가 아닐 경우 False를 return함 

print((1.00002).is_integer())   # 정수가 아님 -> False 
print((1.0000).is_integer())    # 정수임 -> True