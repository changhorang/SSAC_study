# Ch1 파이썬 시작
# Programming : 프로그램을 만드는 것
# Program : 미리 작성된 것
# Computer program : 컴퓨터가 해야할 일을 미리 기술한 것

# binary digit (이진 숫자) : 0 & 1로 이루어진 컴퓨터의 언어
# (Ex) 16 bit... 

# Source code : 프로그래밍 언어로 작성한 프로그램으로 기계가 이해할 수 있게 만듦

# Python
# (Compiler) vs (Interpreter)
# Compiler : 전체 번역 / 실행 파일 생성 / Non-interactive / 개발 시간 길다 / 프로그램 실행시간 빠름
# Interpreter : 실시간, script file (=src file) / Interactive / 개발 시간 짧음 / 상대적 실행시간 느림
# 문장이 여러줄 가능 vs. 일반적으로 문장은 한줄(여러줄도 가능)
# 문장의 끝을 나타내는 기호 vs. 문장의 끝을 나타내는 기호가 없을 수도 있다. (파이썬은 없음)

# 프로그램 성능 기준은 정량적이 아닌 정성적으로 설정
# - ex) 3초 내에 실행 완료,
#         메모리 사용량은 최대 1MB, 
#         이전 프로그램보다 10% 속도 향상

# - ex) 정량적: 프로그램이 느려요, 빨라지게 해주세요.

# Ch1-2
# 파이썬의 문장은 줄바꿈으로 완성 (끝을 나타내는 키워드가 없음)
#  - 문장을 구별하는 기호는 있음 (;)
a = 10; print(a)


# 실행 파일(Executable)
#  - 윈도: 확장자로 구분 - .bat, .com, .exe (3가지 가능)
#  - 유닉스 계열(UNIX, Linux, MAC): 권한(읽기, 쓰기, 실행)으로 구분


# 실행 파일 찾는 순서
#  - 현재 디렉터리
#  - PATH에 등록된 디렉터리를 순차적으로 찾음


# 환경변수(Environment Variable)
#  - 운영체제 : 프로그램이 실행되는 '환경'이라고 간주할 수 있음
#  - 운영체제에 정의하는 변수
#  - 운영체제나 프로그램이 활용하는 변수
#  - 운영체제에서 미리 준비한 환경 변수도 있고 사용자나 프로그램의 필요에 의해 환경변수를 새로 만들 수 있음


# 윈도의 환경변수
#   - PATH: 실행 파일의 경로를 지정하는 환경 변수
#           path 도스 명령어로 확인
#           set 도스 명령어로 설정
#           PATH 환경 변수에 저장된 경로의 구분은 Windows는 세미콜론(;), 유닉스 계열은 콜론(:)


# 윈도 도스 명령어(자세한 내용은 스스로 찾아서 채워넣어보세요)
#  - dir: 현재 디렉토리 파일 리스트 
#  - path: 시스템 및 사용자 환경 변수 리스트
#  - cd: change directory
#  - set: 환경변수 설정하기
#  - cls: 현재 작성한 거 지우기


# 컴퓨터 메모리
#  - 주소(address)로 각 메모리가 구별됨
#  - 바이트 단위로 주소가 지정됨


# 변수
#  - 메모리(주소)에 이름 붙인 것

# 실습
print("Hello coding Python")
print("Hello! " * 3)

# 표현식(Expression, expr)
#  : 최종 결과가 값이 되는 구성(construct)
#    항과 연산자의 조합, 한 개의 항도 표현식을 이룰 수 있음
#    항은 리터럴, 변수, 함수, 객체
# ex) ‘hello’
#     3 * 20
#     2 + a * func1(20)

# 문장 : 기본 실행 단위
#  - 단순문(simple statments)
#    : 13가지 존재(파이썬 https://docs.python.org/3/reference/simple_stmts.html 참고)
#  - 복합문(compound statements)

# 키워드
import keyword
print(keyword.kwlist)

# 식별자 (https://docs.python.org/3/reference/lexical_analysis.html#identifiers 참고)
#  - 특별한 의미를 지닌 식별자
#  1) _* (밑줄로 시작하는 식별자)
#  2) __*__ (밑줄 두개로 시작하고 밑줄 두개로 끝나는 식별자)
#  3) __* (밑줄 두개로 시작하는 식별자)

# snake_case vs. camelCase vs. PascalCase
num_of_apples = 10
price_per_apple = 20
total_payment = num_of_apples * price_per_apple

numOfApples = 10
pricePerApple = 20

NumOfApples = 10
PricePerApple = 20

# 파이썬에서는 관례적으로
#  - 변수, 상수, 함수 식별자는 snake_case
#  - 클래스 식별자는 PascalCase

# 클래스
#  - 사용자 정의 데이터 타입(User-Defined Data Type)


# type 함수
#  - 사용: type(식별자)
#  - 반환값이 <class ‘type’> 이면 해당 식별자는 ‘클래스’
#  - 반환값이 <class ‘function’> 이면 (사용자 정의) ‘함수’
#  - 반환값이 <class 'builtin_function_or_method'> 이면 ‘내장 함수’ 또는 ‘메서드’

# 코드 작성 시에 주석은 간결하게 필요한 만큼만 작성

# 연산자
# 연산자
#  - 단항 연산자 : 우선순위가 굉장히 높다  (-, +, not)
#  - 이항 연산자 :  변수 2개 + 키워드 1개 (*, /, +, -,...)
#  - 삼항 연산자 : '버스' if money > 1250 else '걸어가기' / 변수 3개 + 키워드 2개


# 리터럴(Literal)
#  - 소스 코드에 새긴 값
#  - 변하지 않아요

