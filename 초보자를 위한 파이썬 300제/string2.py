license_plate = "24가 2210"
# 문자열에서는 공백도 문자로 인식하기 때문에 공백도 세야함

# 방법 1
print(license_plate[4], license_plate[5],license_plate
[6], license_plate[7], sep="")

# 방법 2
print(license_plate[4:8])

# 방법 3
print(license_plate[-4:])
# 슬라이싱 안에 문자 음수 넣음
# 그러면 뒤에서 시작해서, 1부터 문자 세서 4번째에 해당하는 문자 즉 2가 해당됨
# 2부터 똑같이 오른쪽으로 셈 
