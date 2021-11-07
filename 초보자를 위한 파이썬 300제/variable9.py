syear = "2020"
year = int(syear)

# 방법 1
print(year - 3)
print(year - 2)
print(year - 1)
print()

# 방법 2
for Y in range(3,0,-1):    # range(큰수,작은수,-1)이라는 점 주의!
    print(year - Y)
print()

# 방법 3
i = 3
while i > 0 :
    print(year - i) 
    i -= 1
 
