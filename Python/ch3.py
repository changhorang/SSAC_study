# Ch3 조건문

# Boolean : True / False
# 비교 연산자
# ==, !=, <, >, <=, >=
print(10 == 100)
print(10 != 100)

# not, and, or
print(not True)
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

# if 조건문
import datetime
now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시작은 {}시로 오전입니다".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 {}시로 오후 입니다".format(now.hour))

# if~else와 elif 구문
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

