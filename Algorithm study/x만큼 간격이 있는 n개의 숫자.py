def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x*i)        
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(2, 5))