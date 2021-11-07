string = "홀짝홀짝홀짝"

# 방법 1
print(string[0], string[2], string[4], sep="")

# 방법 2
print(string[-2], string[-4], string[-6], sep="")

# 방법 3
print(string[::1])
print(string[::2])
print(string[::3])
print(string[::4])
print(string[::-1])
print(string[-3:-6:-1])
print(string[4:1:-1])

# 끝이 양수 : '처음'인덱스부터 '끝'인덱스까지 양수만큼 증가시켰을 때의 값
# 끝이 음수 : '처음'인덱스부터 '끝'인덱스까지 거꾸로 출력
# 끝이 양수일땐 [숫자가 작은 인덱스 : 숫자가 큰 인덱스 : 양수]
# 끝이 음수일땐 [숫자가 큰 인데스 : 숫자가 작은 인덱스 : 음수]

# 양수와 음수는 단순히 세는 방법임
# 오른쪽 부터 세면 -(마이너스)가 붙어 음수로 표시하는 거고,
# 왼쪽 부터 세면 +(플러스)가 붙어 양수로 표시되는 거임.  
# 단 슬라이싱에 들어가는 숫자가 3개일때, 맨 오른쪽에 있는 음수와 양수는 읽는 방법이 됨.