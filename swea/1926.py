T     = int(input())
num = 0

for i in range(1, T+1):
    i = str(i)
    if i.count("3") or i.count("6") or i.count("9"):
        num = i.count("3") + i.count("6") + i.count("9")
        print("-" * num, sep="", end=" ")  
    else:
        print(i, end=" ")
