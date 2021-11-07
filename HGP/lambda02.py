# 변수를 선언합니다. 
list_input_a = [1, 2, 3, 4, 5]

# map() 함수를 사용합니다.
output_a = map(lambda x: x * x, list_input_a)
print("# map() 함수의 실행결과")
print("map(lambda x: x * x, list_input_a):", output_a)          # 실행결과 -> <map object> :  제너레이터
print("map(lambda x: x * x, list_input_a):", list(output_a))
print()

# filter() 함수를 사용합니다. 
output_b = filter(lambda x: x < 3, list_input_a)
print("filter() 함수의 실행결과")
print("filter(lambda x: x < 3, list_input_a):", output_b)       # 실행결과 -> <filter object> :  제너레이터
print("filter(lambda x: x < 3, list_input_a):", list(output_b))