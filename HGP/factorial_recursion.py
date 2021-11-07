# 함수를 선언합니다. 
def factorial(n):
    # n == 0  ->  1 return 
    if n == 0:
        return 1
    # n != 0  ->  n * (n-1)! return  
    else : 
        return n * factorial(n-1)


# 함수를 호출합니다.
print("1!: ", factorial(1))
print("2!: ", factorial(2))
print("3!: ", factorial(3))
print("4!: ", factorial(4))
print("5!: ", factorial(5))
