file_name = "보고서.xls"

# 방법1
file_name1 = file_name.endswith(("xls","xlsx"))     # 문자열 끝이 xls 또는 xlsx로 끝나면 True 반환

print(file_name1)

# .endswith() 메서드는 괄호 안에 문자열이 2개 이상이면, 괄호로 묶어야 함
# ex) file_name = file_name.endswith("xls","xlsx") [오류 발생]