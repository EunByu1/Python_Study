def test(a, b=10, c=100):
    print(a+b+c)

# 1) 기본형태
test(10, 20, 30)

# 2) 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)

# 3) 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b=200)

# 4) 키워드 매개변수로 일부 매개변수만 지정한 형태 
test(10, c=200)

# 5) 한개만 매개변수입력하고 나머지 키워드 매개변수 
test(10)                        # 120
test(10, b=20)                  # 130
test(10, b=20, c=30)            # 60

# 실행 불가능
# test(b=30, 5, c=50)