# 방법_1
value = ord(input())
print(chr(value + 1))


# 방법_2
value = input()

if((value != "z") and (value != "Z")):
    print(chr(ord(value) + 1))
else:
    pass
