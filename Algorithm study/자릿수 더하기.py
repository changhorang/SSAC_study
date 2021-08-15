def solution(n):
    a = str(n)
    answer = 0
    for i in range(len(a)):
        answer += int(a[i])
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(solution(123)))
print("결과 : {}".format(solution(987)))