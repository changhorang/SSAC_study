# Ch5 Function

# 추상(Abstraction)
#  - 사전적 의미 : 여러 가지 사물이나 개념에서 공통되는 특성이나 속성 따위를 추출하여
#                  파악하는 작용.
#  - 객체(Object, 개체) : 여러 가지 사물이나 개념



# Python’s Standard Type Hierarchy
#  : https://docs.python.org/3/reference/datamodel.html#objects-values-and-types#the-standard-type-hierarchy
# 1) None
# 2) NotImplemented (구현이 안되었음)
# 3) Ellipsis (...)
# 4) numbers.Number
#    - numbers.Integral: int, bool
#    - numbers.Real: float
#    - numbers.Complex: complex
# 5) Sequences
#    : finite ordered sets indexed by non-negative numbers
#    - Immutable sequences: Strings, Tuples, Bytes
#      : 요소를 변경할 수 없음
#    - Mutable sequences: Lists, Byte Arrays
# 6) Set types
#    : unordered, finite sets of unique, immutable objects
#      → 정수로 인덱싱될 수 없음
#    - Sets: mutable sets
#    - Frozen sets: immutable sets
# 7) Mappings (사전)
#    : finite sets of objects indexed by arbitrary index sets
#    - Dictionaries
# 8) Callable types
#    - User-defined functions: def 키워드, 반환시 return 문
#    - Instance methods: 클래스 정의 내에서 def 키워드, 반환시 return 문
#    - Generator functions: def 키워드, 반환시 yield 문 ← next() 내장 함수 사용
#    - Coroutine functions:
#    - Built-in functions:  sum(), len()
#    - Built-in methods:  list.append(), dict.get()
#    - Classes:
#    - Class Instances: special method __call__()을 미리 정의해 두어야 함

# 함수 사용 = "함수를 호출한다"
# 매개변수 = 함수에 넣는 여러 자료(?)
# 리턴값 = 함수를 호출해 최종적으로 나오는 결과


print("\nFunction")
def print_n_times(value, n):
    for i in range(n):
        print(value)
print_n_times(1, 5)

# 가변 매개변수 (*values : 매개변수를 원하는 만큼 받을 수 있음) / 기본 매개변수 (built-in 함수)
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
print_n_times(2, "H", "i")

# 함수란?
#   - function: 기능 → 행위 → action, behavior
#   - 함수: 함(상자 함) → B/B, 함수의 입출력에 관심
#   - (관련 있는) 코드 블록에 이름 붙인 것
#   - parameters vs. arguments
#   - 함수 헤더(Function signature: 반환타입, 함수이름, 함수인자)와 함수 바디로 구성

# 파이썬에서 함수 정의
#   - def 키워드 사용
#   - 함수 헤더에 반환 타입(X)

# 함수를 사용하는 이유
#   - 코드 중복 제거
#   - 프로그램을 기능별로 구분 → 모듈화

# 파이썬의 arguments 또는 parameters
#   1) 위치 인자/매개변수(positional ~~~): 인자/매개변수의 위치로 값 지정 (순서가 중요)
#   2) 키워드 인자/매개변수(keyword ~~~): 인자/매개변수의 이름으로 값 지정
# (순서는 중요하지 않음)

# 가변 매개변수
#   : 매개변수 이름 앞에 *를 붙임 → 위치 매개변수로 인식
#   : 매개변수의 개수가 정해지지 않음, 필요한 만큼의 인자를 받음
#   - 대표적인 예: print()
#   - 제약: 1) 일반 매개변수 선언이 끝난 후에 가변 매개변수 정의
#           2) 가변 매개변수는 1개만 가능
#   - 함수 내에서 튜플 객체
#   - 함수 호출 시 가변 매개변수를 키워드 지정 방식으로 사용할 수 없음

# 기본 매개변수(Default parameters)
#   : 인자가 생략될 때 해당 매개변수의 초깃값으로 적용
#   - 키워드 인자로 호출될 때 유용
#   - 기본 매개변수는 일반 매개변수 이후에 정의

# 함수 호출 시 인자 지정 방식
#   1) 위치 지정 방식
#     - 매개변수의 식별자를 이용하지 않음
#     - 인자의 순서가 중요
#   2) 키워드 지정 방식
#     - 매개변수의 식별자를 이용
#     - 인자의 순서는 중요하지 않음
#   3) 위치, 키워드 혼용 방식
#     - "위치 인자"를 "키워드 인자"보다 "먼저!" 기술
#   4) 기본 매개변수와 위치 지정 방식 
#   5) 기본 매개변수와 키워드 지정 방식 : 키워드는 마지막으로
#   6) 기본 매개변수와 위치 및 키워드 지정 방식 혼용 : 키워드는 마지막으로


# 가변 키워드 인자
#   - cf.) 가변 매개변수를 가변 인자라고도 일컬음
#          가변 인자: 위치 매개변수
#   - 가변 키워드 인자: 키워드 매개변수
#   - 매개변수 이름 앞에 ** 붙임
#   - 함수 내부에서 Dictionary로 처리
print("\n가변 키워드 인자 예시")
def print_all(title, n=2, **kwargs):
    print('kwargs = {}'.format(kwargs))
    print('type of kwargs = {}'.format(type(kwargs)))
    print('title = {}'.format(title))
    print('n = {}'.format(n))
print_all('예제', name = '홍길동', age =22, hobby = ['의적', '호부호형'])

# 가변 키워드 인자 활용법
#   - wrapper 함수
#   - 다른 함수를 호출할 때
print("\n가변 키워드 인자 활용")
def my_func(*args):
    print(args)
    for arg in args:
        print(arg)
my_func(10, 'a', 'hello', [1, 2, 3], range(100))
my_func('abc', 10)

def my_func(**kwargs):
    print(kwargs)
    for p_name, p_value in kwargs.items():
        print('{}, {}'.format(p_name, p_value))
my_func(name = '홍길동', age = 22, score = 'A')
my_func(name = 'None', height = 100, weight = 50)

# Packing vs. Unpacking
#   * Packing
#    : 인자로 받은 여러 개의 값을 하나의 매개변수로 받을 수 있게 하는 매커니즘
#      - Positional argument packing: *args → 튜플로 받음
#      - Keyword argument packing: **kwargs → 딕셔너리로 받음
print("\nPacking")
def print_family_name(*parents, **sibling):
      print("아버지 :", parents[0])
      print("어머니 :", parents[1])
      if sibling:
          print("호적 메이트..")
          for title, name in sibling.items():
              print('{} : {}'.format(title, name))
print_family_name("홍길동", '심사임당', 누나='김태희', 여동생='윤아')

#   * Unpacking
#    : 하나의 변수에 담긴 여러 개의 값을 여러 인자로 풀어주는 매커니즘
#      - Positional argument unpacking: 함수 호출 시 인자(튜플, 리스트) 앞에 *
#      - Keyword argument unpacking: 함수 호출 시 인자(딕셔너리) 앞에 **
print("\nUnpacking")
def my_sum(x, y, z):
    return x + y + z
values = (10, 20, -40)
print(my_sum(*values))

def print_all(name, age, job):
    print(name, age, job)
student = {'name' : 'kim', 'job': '-', 'age' : 30}
je = {'name' : 'chan','age' : 33, 'job': '12'}
print_all(**student)
print_all(**je)