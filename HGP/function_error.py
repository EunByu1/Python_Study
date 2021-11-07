# TypeError 발생 

def print_n_times(value,n):
    for i in range(n):
        print(value)

# 함수를 호출합니다.
# 매개변수로 하나의 값만 넣음
print_n_times("안녕하세요")  

# 매개변수로 세개의 값을 넣음
print_n_times("안녕하세요", 10, 20)

