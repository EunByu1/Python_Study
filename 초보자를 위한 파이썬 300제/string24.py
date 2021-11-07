# .endswith("문자열")
file_name = "보고서.xlsx"

# 방법1
file = "xlsx" in file_name
print(file)

# 방법2
print(file_name.endswith("xlse"))   # 문자열 끝에 xlsx가 존재하면, True 반환