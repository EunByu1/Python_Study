# try except 구문을 사용합니다. 
try:
    # 파일을 엽니다.
    file = open("info.txt", "w")
    # 여러 가지 처리를 수행합니다.
    # 파일을 닫습니다. 
    file.close()

except Exception as e:
    print(e)


print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)


# except [발생 오류[as 오류 메시지 변수]]:
try:
    a = int(input("정수입력: "))
    print( 45 /a )

except ValueError as ec:    
    # ValueError 발생 시, ValueError가 발생한 이유에 대해 설명하는 변수 : ec
    print("변수 문제:", ec)

except ZeroDivisionError as why:
    # ZeroDivisionError 발생 시, ZeroDivisionError가 발생한 이유에 대해 설명하는 변수 : why
    print("0으로 나누었음:", why)

else:
    print("성공")  