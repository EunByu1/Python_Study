icecream = {
    '탱크보이': 1200, 
    '폴라포': 1200, 
    '빵빠레': 1800, 
    '월드콘': 1500, 
    '메로나': 1000
}

# 방법1
keys = []
for key in icecream.keys():
    keys.append(key)

print(keys)

# 방법2
ice = list(icecream.keys())
# list()함수를 안써주게 되면, 
# dict_keys(['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나']) 로 출력됨.
print(ice)