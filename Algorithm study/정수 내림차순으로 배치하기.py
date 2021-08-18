def solution(n):
    answer = int("".join(sorted(str(n), reverse = True)))
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(123568))