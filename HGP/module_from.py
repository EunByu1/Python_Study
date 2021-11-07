# -----------------------------------------------------------------
# 방법 1
from math import sin, cos, tan, floor, ceil
# 형식
# from 모듈이름 import 가져오고 싶은 변수(들) or 함수(들)

# 삼각함수 
print("sin(1) : %.3f" % sin(1))
print("cos(1) : %.3f" % cos(1))
print("tan(1) : %.3f" % tan(1))
print()

print("실수를 정수로 변환하는 방법")
# 실수를 정수로 변환해줄 때 반올림 X
print("floor(2.5) : %d " % floor(2.5))
# 실수를 정수로 변환해줄 때 반올림 O
print("ceil(2.5)  : %d " % ceil(2.5))

print()
print("-----------------------------------------")
print()
# -----------------------------------------------------------------
# 방법2
from math import *
# form math import * : math 모듈 내부에 있는 모든 것을 가져온다는 뜻 

# 삼각함수
print("sin(1) : %.3f" % sin(1))
print("cos(1) : %.3f" % cos(1))
print("tan(1) : %.3f" % tan(1))
print()

print("실수를 정수로 변환하는 방법")
# 실수를 정수로 변환해줄 때 반올림 X
print("floor(2.5) : %d " % floor(2.5))
# 실수를 정수로 변환해줄 때 반올림 O
print("ceil(2.5)  : %d " % ceil(2.5))