keys = ("apple", "pear", "peach")
vals = (3300, 250, 400)

print(zip(keys, vals))          # 실행결과 -> <zip object> : 제너레이터 
print(list(zip(keys, vals)))    # 실행결과 -> 튜플로 묶어서 리스트 형태로 출력
print(dict(zip(keys, vals)))    # 실행결과 -> 딕셔너리 형태로 출력 