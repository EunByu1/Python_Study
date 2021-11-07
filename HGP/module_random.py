import random
print("# random 모듈")

# random(): 0.0 <= x < 1.0 사이의 float를 return
# 0 ~ 1 범위의 실수 난수 생성 
print("- random():", random.random())
print()

# uniform(min, max): 지정한 범위 사이의 float를 returnm
print("- uniform(10, 20):", random.uniform(10,20))
print()

# randint(): 정수 난수 생성
print("- randint(10):", random.randint(0, 10))
print()

# randrange(): 지정한 범위의 int를 return
# - randrange(max): 0 ~ max사이의 값을 return
# - randrange(min, max): min ~ max사이의 값을 return 
# 지정한 범위의 정수 난수 생성
print("- randrange(10):", random.randrange(10))
# 1에서부터 시작하여 10씩 더한 값이 100미만
print("- randrange(0, 100, 10):", random.randrange(1, 100, 10))     
print()

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 섞음
print("- choice([1, 2, 3, 4, 5]:", random.choice([1, 2, 3, 4, 5]))
print()

# shuffle(list): 리스트의 요소들을 랜덤하게 섞음
print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))
print()

# sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑음
print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k = 2))
