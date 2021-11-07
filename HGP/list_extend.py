# 리스트 평탄화
# 함수를 선언한다.
def flatten(data):
    temp = []
    output = []

    for i in data:
        if type(i) == list:
            # 리스트에서 +=는  extened랑 같다.
            temp += i 
            # ex) i가 [1,2,3]이면, 대괄호 없어진채로 요소듣만 temp에 저장됨 -> temp = [1,2,3]
        else:
            temp += [i]

    for i in temp:
        if type(i) == list:
            output += i
        else :
            output += [i] 

    return output

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:", example)
print("변환:", flatten(example))

# ----------------------------------------------------------------------------------------
# 리스트 평탄화
# 함수를 선언한다.
def flatten(data):
    output = []

    for i in data:
        if type(i) == list:
            # 리스트에서 +=는  extened랑 같다.
            # 재귀함수 
            output += flatten(i) 
        else:
            output += [i]
    return output            

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:", example)
print("변환:", flatten(example))