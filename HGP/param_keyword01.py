# 키워드 매개변수 
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
    
        print()


# 함수를 호출합니다.
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)