icecream = {
    '탱크보이': 1200, 
    '폴라포': 1200, 
    '빵빠레': 1800, 
    '월드콘': 1500, 
    '메로나': 1000
}

# 방법1
price_1 = 0
for v in icecream.values():
    price_1 += v

print(price_1)

# 방법2
print(sum(icecream.values()))