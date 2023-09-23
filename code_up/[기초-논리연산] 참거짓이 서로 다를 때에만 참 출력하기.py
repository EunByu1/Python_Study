num1, num2 = map(int, input().split())
num1, num2 = bool(num1), bool(num2)

if (num1 == True and num2 != True) or (num1 != True and num2 == True):
    print("True")
else:
    print("False")
