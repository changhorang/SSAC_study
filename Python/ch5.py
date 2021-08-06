# Ch5 Function
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

