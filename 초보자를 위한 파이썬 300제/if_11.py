value = int(input("score: "))

if (81 <= value <= 100):
    print("grade is A")
elif (61 <= value <= 80):
    print("grade is B")
elif (41 <= value <= 60):
    print("grade is C")
elif (21 <= value <= 40):
    print("grade is D")
else:
    print("grade is E")
