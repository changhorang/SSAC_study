def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer

# 실행을 위한 테스트코드입니다.
print(solution(12))
print(solution(5))