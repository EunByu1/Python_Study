ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500,
       '오징어': [1,2,3]}

# 딕셔너리에서 메로나 삭제
del ice["메로나"]
print(ice)

# .pop()은 리스트에서만 사용가능!
ice["오징어"].pop(1)
print(ice)
