# 방법1
user   = input("주민등록번호: ").split("-")
First  = user[0]
Second = user[1]

Course1 = (int(First[0])*2) + (int(First[1])*3) + (int(First[2])*4) + (int(First[3])*5) + (int(First[4])*6) + (int(First[5])*7)
Course2 = (int(Second[0])*8) + (int(Second[1])*9) + (int(Second[2])*2) + (int(Second[3])*3) + (int(Second[4])*4) + (int(Second[5])*5)
Course3 = (Course1 + Course2) % 11
Course4 = 11 - Course3

if int(Second[-1]) != Course4:
    print("유효하지 않은 주민등록번호입니다.")
else:
    print("유효한 주민등록번호입니다.")
