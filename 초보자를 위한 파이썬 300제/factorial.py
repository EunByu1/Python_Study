def fact(n):
    if n==1:
        return 1
    else:
        return fact(n-1)*n

a = int(input(""))
print(fact(a))