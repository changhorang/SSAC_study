# Ch2 자료형과 문자열
# 1. 문자열 (string) : "abcd"...
# 2. 숫자 (number) : 1, 2, 3,...
# 3. 불 (boolean) : True, False

print(type(273.0)) # float
print(type(273)) # int
print(type("hello")) # str

# "" 넣기 : ''&"" 동시 사용 또는 아래와 같이 사용
print("\"h\"ello") # "h"ello

# \n : 줄바꿈
# \t : tab 추가
# "" + "" : 문자열 연결 (같은 타입끼리)
# "" * int : 문자열 반복

# [] 인덱싱 / [:] 슬라이싱
# len() : 문자열의 길이 반환

# 숫자
# int (정수) / float (실수)
# 연산자 : +, -, *, /, // (소수점 제거), % (나머지 연산자), **
print(17//3)
# 연산자 우선 순위
# TypeError : 다른 타입끼리 충돌