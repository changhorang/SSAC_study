# Ch3 조건문

# Boolean : True / False
# 비교 연산자
# ==, !=, <, >, <=, >=
print(10 == 100)
print(10 != 100)

# 문자열 비교
#  - 순서는 문자셋 → ASCII, Unicode(UTF-8), EUC-KR, KSC-5601, CP949
#  - 알파벳 순, 가나다 순
#  - 특수문자는 보통 잘 비교 안함
#  - 왼쪽 문자부터 비교 시작하다가 결판이 나면 비교 종료
print("\n문자열 비교")
print("가방" < "하마")
print("apple" < "banana")

# not, and, or
print("\n논리연산자")
print(not True)
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

# if 조건문
print("\nif 조건문")
import datetime
now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시작은 {}시로 오전입니다".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 {}시로 오후 입니다".format(now.hour))

# if~else와 elif 구문
print("\nif~else와 elif 구문")
number = int(input("정수>"))

if number % 2 == 0:
    print("짝수")

else :
    print("홀수")

month = now.month
if 3 <= month <= 5:
    print("spring")
elif 6 <= month <= 8:
    print("summer")
elif 9<= month <= 11:
    print("autum")
else:
    print("winter")

# False로 변환되는 값 (Truth Value Testing)
#  - 값만으로 True, False를 결정하는 것

#  - False로 테스팅되는 것
#     1) 상수 중에서는 None, False
#     2) 수치 데이터 중 제로: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
#     3) 빈 시퀀스, 빈 컬렉션: ‘’, “”, (), [], {}, set(), range(0)
#  - 위 이외는 무조건 True로 판단

# pass 키워드 (pass statement)
#  - 빈 코드 블록이 필요할 때
#  - 다른 언어에서는 {}
#  - 파이썬은 빈 코드 블록을 허용하지 않음 (반드시 문장이 존재해야 함)
# raise NotImplementError를 발생 시키는 것도 하나의 방법

# 실습 코드
x = 11
if 10 < x < 20:
    print("조건에 맞음")