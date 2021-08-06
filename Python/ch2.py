# Ch2 자료형과 문자열
# 1. 문자열 (string) : "abcd"...
# 2. 숫자 (number) : 1, 2, 3,...
# 3. 불 (boolean) : True, False

print(type(273.0)) # float
print(type(273)) # int
print(type("hello")) # str

# 이스케이프 문자(Escape Character, 탈출 문자)
#  - 백슬래시와 함께 사용하는 문자: \n, \”, \’, \\
#  - 백슬래시의 역할: 특수 문자의 특별한 임무를 제거(탈출)

# 문자열을 날것 그대로 표현하고 싶을 때
#  - 문자열 앞(따옴표 왼쪽)에 r
print(r"he \n ll \t o")

# "" 넣기 : ''&"" 동시 사용 또는 아래와 같이 사용
# \", \' : 큰 따옴표, 작은 따옴표 
print("\"h\"ello") # "h"ello

# \n : 줄바꿈
# \t : tab 추가
# "" + "" : 문자열 연결 (같은 타입끼리)
# "" * int : 문자열 반복

"""-------------------------------------------------------------------------"""

# [] 인덱싱 / [:] 슬라이싱
# 슬라이싱(Slicing) 
#  - 원소의 범위를 지정(시작과 끝)하여 전체 데이터에서 일부를 취하는 방식
#  - [시작 인덱스:종료 인덱스]
#  - 종료 인덱스는 포함되지 않음
#  - 슬라이싱 결과는 원본 데이터 타입과 동일

print("안녕하세요"[1:4]) # 녕하세
print("안녕하세요"[1:]) # 녕하세요
print("안녕하세요"[:3]) # 안녕하

# 대입연산자(Assignment Operator)
#  - 이항 연산자
#  - 왼쪽에는 반드시 변수
#  - 오른쪽에는 반드시 값(표현식)
#  - 모든 연산자를 통틀어서 우선순위가 제일 낮다
#  - 대입연산자가 여러개 일 때 연산 순서는 오른쪽에서 왼쪽으로
#   Ex) a = b = c = 100

# 바인딩(Binding)
#  - 대입연산자로 변수에 값(객체)를 대입하는 것을 파이썬에는 ‘변수를 객체에 
#    바인딩한다’고 표현

# 변수 = 표현식
#  = 표현식의 결과(값, 객체)를 변수에 바인딩한다.
#  = 변수가 값(객체)를 참조한다.


# len() : 문자열의 길이 반환
a_list = [1,2,3]
len(a_list)

"""-------------------------------------------------------------------------"""

# 숫자
# int (정수) / float (실수)
# 연산자 : +, -, *, /, // (소수점 제거), % (나머지 연산자), **
print(17//3)
# 연산자 우선 순위
# TypeError : 다른 타입끼리 충돌

# 연산자 우선순위
#  : [참조] https://dojang.io/mod/page/view.php?id=2461

# 개략적으로
#  1) 사칙연산자
#  2) 비교연산자
#  3) 논리연산자
#  4) 대입연산자
#    Ex) if price > 100 and money == 100/num_of_person

"""-------------------------------------------------------------------------"""

# 변수
#  - 메모리(주소)에 이름 붙인 것
#  - 이름을 붙였기 때문에 부를 수 있고 따라서 데이터를 재사용하려는 의도가 
#    숨겨져 있다.
#  - 변수에 저장되는 내용에 따라
#     - (일반) 변수: 데이터(객체)가 직접 저장됨
#     - 참조(reference) 변수: 데이터가(객체) 저장된 메모리의 주소가 저장
#  - 파이썬의 변수는 모두 참조 변수이며 “객체를 바인딩한다” 라고 표현

# 변수의 필수단계
#  - 선언 : 변수를 준비하는 단계, 이름 붙이기 (메모리를 할당 여부는 언어마다 다름)
#  - 초기화 : 변수에 값(객체)를 저장 또는 바인딩하는 단계
#  - 참조 : 변수에 접근하는 단계
#    - 변수에 저장 / 바인딩된 값(객체)를 사용
#    - 변수에 새로운 값(객체)를 저장/바인딩
#  - 대부분의 프로그래밍 언어에서는 참조하기 전에 반드시 변수 초기화가 필요
#  - 파이썬도 초기화 없이 참조하면 Error 발생

# 파이썬에서 변수의 특징
#  - 파이썬은 변수 선언 단계가 없음
#  - 변수를 선언과 초기화를 동시에 진행
#  - 변수 초기화시 변수 데이터 타입을 명시하지 않음
#  - 파이썬은 변수에 데이터 타입을 지정하지 않음
#    -> 파이썬은 동적 타입 언어

# 동적 타입 언어 vs 정적 타입 언어
#  - 동적 타입 언어 : 프로그램 실행 중에 변수의 타입이 결정
#  - 정적 타입 언어 : 프로그램 컴파일 중에 변수의 타입이 결정 (컴파일러)
#                    한번 결정된 변수의 타입이 프로그램 실행중에 변경되지 않음 

# 강타입(Strong type) 언어 vs. 약타입(Weak type) 언어
#  - 강타입: 연산 등에서 타입이 중요
#  - 파이썬은 강타입 언어

# 동적 (Dynamic) vs 정적 (Static)
#  -> Run-time vs Compilation (Non Run-tiem)
#  - 실행중에 수정 vs 컴파일을 만든 후 실행

# Namespace (이름공간)
#  - 각종 식별자를 모아둔 것
#  - 파이썬의 dir() 함수를 사용하면 현재 Interactive Shell 또는 특정 객체의 
#    Namespace를 리스트로 반환

# 변수와 입력
pi = 3.14
r = 2
print(pi)
print("원주율 = ", pi)
print("반지름 = ", r)
print("원의 둘레 = ", 2*pi*r)
print("원의 넓이 = ", r**2*pi)


# 복합대입연산자
#  - 대입연산자와 이항연산자를 결합한 연산자
#  - x = x 연산자 y ⇒ x 연산자= y
#    ex)  x += 2  ⇒ x = x + 2
#          x //= 3 ⇒ x = x // 3    x = 3 // x (X)
# +=, -=, *=, /=, %=, **=
a = 1
a += 10
print(a)

# input() 사용자 입력
# input을 통해 받는 입력값은 다 string (boolean도 예외 없음)
b = input("Hello?")

print(type(b))

# 데이터 형 변환(데이터 타입 변환)
#  - Type Conversion, Type Cast, Type Casting
#  - 목적: 데이터 타입을 맞추어서 연산을 하기 위함

# Cast : int() / float() / str() 등의 함수를 통해서 자료형 변형
string_a = input("정수")
int_a = int(string_a)

string_b = input("실수")
int_b = float(string_b)

print(type(int_a), type(int_b))

num_input = float(input("숫자 입력>"))

print(num_input, "inch")
print((num_input*2.54), "cm")

num_input1 = int(input("원의 반지름 입력"))

print("\n반지름", num_input1)
print("둘레", 2*pi*num_input1)
print("넓이", pi*num_input1**2)

# 변수 스왑(Swapping)
#  - 두 변수의 내용을 서로 바꾸는 연산
#  - [일반적, 다른 프로그래밍 언어]: 임시 변수 필요, 문장 3개 필요
#  - 파이썬: 문장 1개로 충분 (tuple)
x = 10
y = "hello"

x, y = y, x


# 문자열의 format() 메서드 : str type으로 변환
# format 외의 방식 (%d : 정수, %s : string)

#  - 문자열 내에 {}를 이용하여 출력할 내용의 위치와 형식을 표현
#  - IndexError 발생: {}의 개수보다 출력 인자의 개수가 적을 때

print('price is %d, and name is %s' % (100, 'hello'))

string_c = "{}".format(10)

print(string_c)
print(type(string_c))

format_d = "{} {} {}".format(1, "문자열", True)
print(format_d)

# leading zeroes, trailing zeroes
# leading spaces, trailing spaces
# d : decimal  / f : float / 자릿수 초과시 소수점은 반올림, 정수 부분은 그대로 다 표현
format_e1 = "hello {:5d}".format(10)
print(format_e1)
format_e2 = "hello {:5f}".format(10.512345)
print(format_e2)
format_e3 = "hello {:5.3f}".format(10.512345)
print(format_e3)
format_e4 = "hello {:.3f}".format(10.512345)
print(format_e4)

# {} 설명 추가 / 인자 재사용
#  위치 지정과 이름 지정의 차이 : 이름 지정 방식은 인자의 순서를 무시할 수 있음
# 위치 지정 방식과 이름 지정 방식의 혼용 
#  - format 메서드의 인자로 위치 지정 방식의 인자를 반드시 먼저 다 기술한 후
#    이름 지정 방식의 인자를 나열한다.
print('{1} {name} {0} {job}'.format(10, 20, job='a', name='n'))


#  1) 위치 지정
#  - {position} : 인자의 위치값(정수)
print('{1}은(는) {0}보다 강하다. {1}'.format('펜', '칼'))
#  2) 이름 지정
#  - {identifier}: 인자의 이름
print('이름 : {name} \n직업 :{job} \n닉네임 : {name}'.format(name = "Hi", job = "Hello"))

# f-string (Formatted String Literal) : Python 3.6 NF
#  - 문자열의 format 메서드를 쓰지 않고 formatting 할 수 있음
#  - 대신 이름 지정 방식으로만 사용할 수 있고 변수가 필요하다.
#  - 형식: 문자열을 왼쪽에 f 추가
#  - 변수를 통해서 출력할 내용을 간접적으로 전달
obj1 = "펜"
obj2 = "칼"
print(f'{obj1}은(는) {obj2}보다 강하다.')

# 정렬(Alignment)
#  - <, >, ^ : 좌측, 우측, 가운데 정렬
#  - 숫자는 기본적으로 우측정렬
#  - 그외 객체는 좌측정렬
#  ex)
#  >>> '이름: {:10}, 사번: {:10}'.format('홍길동', 1234) 


# 대소문자 바꾸기 : upper(), lower()
f = "hello"
g = f.upper()
print(g)
print(g.lower())

# strip(), lstrip(), rstrip() 메서드
#  - 인자가 없으면: Whitespace(space, tab, 줄바꿈 등) 제거
#  - 인자를 문자열로 받으면: 해당 문자열을 구성하는 문자들을 제거

input_a = """
   Hi   """
print(input_a)
print(input_a.strip())

# 문자열 찾기 : find() & rfind()
input_b = "안녕안녕".find("안녕")
input_c = "안녕안녕".find("안녕")
print(input_b)
print(input_c)

# 문자열 자르기 : split()
a = "10 20 30 40".split(" ")
b = "10/20/30/40".split("/")
print(a)
print(b)

# 실습 코드
a = input("> 1번째 숫자: ")
b = input("> 2번째 숫자: ")
print("\n{} + {} = {}".format(a, b, int(a)+int(b)))

string = "hello"
print("A 지점: ", string)
print("B 지점: ", string.upper())