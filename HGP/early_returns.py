# ------------------------------------------------------
# 피보나치 수열 방법 1

# 메모화 기술
dictionary = {
    1:1,
    2:1
}

# 함수를 선언합니다.
def fibonacci(n):
    if n in dictionary:
        # 메모되어 있으면, 메모된 값을 return
        return dictionary[n]
    else:
        # 메모되어 있지 않으면, 값을 구함
        output = fibonacci(n-1)+ fibonacci(n-2)
        dictionary[n] = output
        return output

# 함수를 호출합니다. 
print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))
# ------------------------------------------------------

# ------------------------------------------------------
# 피보나치 수열 방법 2

# 메모화 기술
dictionary = {
    1:1,
    2:1
}

# 함수를 선언합니다. 
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]

    output = fibonacci(n-1) + fibonacci(n-2)
    dictionary[n] = output
    return output

# 함수를 호출합니다. 
print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))
