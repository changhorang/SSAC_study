# 반복문
# list / element / index
# 리스트(list) 자료형
#  - 여러 자료를 함께 보관/관리
#  - 자료의 저장 순서가 있음(시퀀스 자료형)
#  - 0부터 시작하는 정수 인덱스
#  - 리스트에 저장되는 자료들은 같은 자료형이 아니어도 된다
#     cf) 배열: 같은 자료형만 여러개 저장하는 시퀀스 자료 구조
#  - mutable 객체(자료형): 요소 변경 가능
#     cf) immutable 객체: tuple, 문자열
#  - 데이터 중복 허용: 같은 값의 요소를 여러 개 가질 수 있다
#    cf) 데이터 중복 허용하지 않는 자료형: set() - 집합
#        Key의 중복을 허용하지 않는 자료형: dict()


list_a = [12, 23, 34, "string", True]
print(list_a[3][0])

list_a = [[1, 2, 3], [2,4,5]]
print(list_a[1][1])

# list() 클래스로 리스트 객체 생성
#  - list()의 인자로 리스트, 튜플, 문자열을 입력
list_a = list("hello")
print(list_a)

# element 추가 : append(), insert() (list의 method임)
list_a = [1,2,3]

list_a.append(4)
list_a.append(5)

print(list_a) # [1,2,3,4,5]

list_a.insert(0,10) # [10,1,2,3,4,5]

# extend() : 여러 요소 한 번에 추가
list_a = [1,2,3]
list_a.extend([4,5,6])
print(list_a) # [1,2,3,4,5,6]

# 파괴적 (리스트의 append(), insert(), extend()) vs 비파괴적 (연산자 "+"...): 원본에 영향을 주는지 여부

# 리스트 element 제거 : del , pop() 
# * del은 함수가 아닌 문장으로 내장함수처럼 사용 불가능
# del 키워드, del 문
#   - 식별자(변수, 함수, 클래스), 요소 제거
#   - namespace에서 해당 식별자 제거
# * pop은 값을 꺼내오는 것

# 1) index로 제거
print("\ndel , pop(), remove, clear")
list_a = [0,1,2,3,4,5]
del list_a[1]
print("list_a[1]: ", list_a)

list_a.pop(2)
print("list_a.pop(2): ", list_a)

# 2) 값으로 제거 (처음 찾은 요소 삭제)
list_a = [0,1,2,2,3,3]
list_a.remove(2) # [0,1,2,3,3]

list_a.clear() # [] : list는 남아 있음

# 리스트 내부에 있는지 확인 : in/not in
print("\nin / not in")
list_a = [273, 32, 103, 57, 52]
print(273 in list_a)
print(1 not in list_a)

# for 반복문 : i는 임시 생성자가 아니라서 사라지지 않음
print("\nfor")
for i in range(3):
    print("for 출력")
print(i)
    
for chracter in "hello":
    print("-", chracter)

# Dictionary & 반복문
# list : index 기반으로 값을 저장 / dictionary : key를 기반으로 값을 저장
print("\nDictionary")

dict_a = {
    "key1" : ["value1", "value2", "value3"],
    "key2" : ["value4", "value5", "value6"],
    "key3" : ["value8", "value7"],
    "key4" : "value9"
}

print(dict_a["key4"])

dict_a["key1"] = "value10" # value 추가
dict_a["key4"] = "value9-1" # replace
del dict_a["key3"]
print(dict_a)

# in keyword
print("\nin keyword")
key = input("접근 하고자 하는 key: ")
if key in dict_a:
    print(dict_a[key])
else:
    print("non-existing key")

# get()
print("\nget()")
value = dict_a.get("non-existing key")
print("값: ", value)

if value == None:
    print("존재 안하는 키에 접근") # Keyerror 발생시키지 않고 None 출력

# for 반복문
print("\nfor 반복문")
for key in dict_a:
    print(key, ":", dict_a[key])

# 반복문과 while 반복문
print("\n반복문과 while 반복문")
# range
print("\nrange")
a = range(0, 5)
print(list(a))

n = 12
a = range(0, int(n/2))
print(list(a))

# for
print("\nfor")
array = [6,7,8,9,10]
for i in range(len(array)):
    print("{} 번째 반복, {}".format(i, array[i]))

# 반대로 반복
print("\n역반복문")
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))

# while 반복문
print("\nwhile 반복문 (for)")
i = 0
while i < 10:
    print("{}번째 반복".format(i))
    i += 1

print("\nwhile 반복문 (상태)")
list_test = [1,2,1,2]
value = 2

while value in list_test:
    list_test.remove(value)
print(list_test)

print("\nwhile 반복문 (시간기반 반복)")
import time
number = 0
target_tick = time.time() + 10
while time.time() < target_tick:
    number += 1

print(time.time())
print("10초 동안 {}번 반복".format(number))

print("\nwhile 반복문 (break)")
i = 0
while True:
    print("{}번째 반복문".format(i))
    i += 1
    input_text = input("종료?(y/n): ")
    if input_text in ["y", "Y"]:
        print("end")
        break

print("\nwhile 반복문 (continue)")
numbers = [1,2,5,20,7,8,10,16]

for number in numbers:
    if number < 10:
        continue
    print(number)

# 리스트에 적용할 수 있는 기본 함수 : min(), max(), sum()
print("\nmin(), max(), sum()")
num = [103, 52, 273, 32, 77]
min(num) # 32
max(num) # 273
sum(num) # 537

print("\nreversed()")
num_reversed = reversed(num) # [77, 32, 273, 52, 103]

# enunerate() : list의 요소 반복시 인덱스가 몇 번째인지 확인 가능, for와 조합해 사용
print("\nenunerate()")
example_list = ["A", "B", "C"]
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}이다.".format(i, value))

# dict items()와 반복문 조합
print("\ndict items()와 반복문 조합")
example_dictionary = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}

for key, element in example_dictionary.items():
    print("dict_[{}] : {}".format(key, element))

#리스트 내포
print("\nlist 내포")
array1 = [i*i for i in range(0, 20, 2)]
print(array1)

array2 = [i*i for i in range(0, 20, 2) if i != 0]
print(array2)