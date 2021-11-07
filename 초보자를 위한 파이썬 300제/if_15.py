# 방법 1
pone_num = input("우편번호: ")

if pone_num.startswith("010"):
    print("강북구")
elif pone_num.startswith("011"):
    print("강북구")
elif pone_num.startswith("012"):
    print("강북구")
elif pone_num.startswith("013"):
    print("도봉구")
elif pone_num.startswith("014"):
    print("도봉구")
elif pone_num.startswith("015"):
    print("도봉구")
elif pone_num.startswith("016"):
    print("노원구")
elif pone_num.startswith("017"):
    print("노원구")
elif pone_num.startswith("018"):
    print("노원구")
else:
    print("노원구")

# 방법 2
pone_num = input("우편번호: ")
if pone_num.startswith(("010", "011", "012")):
    print("강북구")
elif pone_num.startswith(("013", "014", "015")):
    print("도봉구")
elif pone_num.startswith(("016", "017", "018", "019")):
    print("노원구")

# 방법 3
pone_num = input("우편변호: ")
pone_num = pone_num[:3]

if pone_num in ["010", "011", "012"]:   
    print("강북구")
elif pone_num in ["013", "014", "015"]:
    print("도봉구")
else:
    print("노원구")