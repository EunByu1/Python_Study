num_str = "720"
print("변환 전 num_str :", num_str,",",type(num_str))
num_str = int("720")    # 형 변환
print("변환 후 num_str :", num_str,",",type(num_str))
# num_str과 바인딩 되어있던 문자열 720이 int()함수로 인해 숫자 720으로 바뀜 = 파괴적 함수


# 변수 2개 사용방법
num_str = "720"
num_int = int(num_str)
print(num_int, type(num_int)) 
# (num_int + 숫자) 연산 가능 
# 이때의 +는 숫자 연산자

print(num_str+"A", type(num_str))
# 이때의 +는 문자 연결 연산자