# p.188 연습문제
key = ["a", "b", "c", "d", "e"]
value = [1, 2, 3, 4, 5]
key_value = {}

for i in range(len(key)):
    key_value[key[i]] = value[i]
print(key_value)

""""""

limit = 10000
i = 1

sum_value = 0
while sum_value <= limit:
    sum_value += i
    i += 1
    
print("{}를 더할 때, {}를 넘으며 그 때의 값은 {}이다.".format(i-1, limit, sum_value))

""""""

max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    mult = i * j
    if mult > max_value:
        max_value = mult
        value = [i, j]

print("최대가 되는 경우 : {} * {} = {}".format(value[0], value[1], max_value))

# 변수의 Scope, 변수의 Lifecycle
#  - 변수는 선언 또는 초기화될 때 접근 가능
#  - 선언된 코드 블록을 벗어나면 삭제됨
#  - 파이썬의 경우
#    : 함수가 종료되면 함수의 변수인 지역변수(로컬 변수)는 삭제되지만
#      복합문 내에서 선언된 지역 변수는 복합문의 코드 블록을 벗어나도 사라지지 않음
