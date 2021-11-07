# %formatting 사용하여 출력
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

# 방법1
print("이름:", name1, "나이:", age1)
print("이름:", name2, "나이:", age2)

# 방법2
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# LAB
print("파이: %.2f" % 3.14)
print("이름: %s" % "초코파이")
print("파이: %.2f 이름: %s" % (3.14, "초코파이"))