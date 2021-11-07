def exp(x,y):
    value = 1
    count = 0
    for i in range(1,y+1):
        value *= x

    
    return value 

val1 = int(input("첫번째 값을 넣으세요:"))
val2 = int(input("두번째 값을 넣으세요:"))

print(exp(val1,val2))