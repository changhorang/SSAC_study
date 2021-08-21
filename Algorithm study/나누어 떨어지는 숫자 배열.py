def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer = sorted(answer)
    if len(answer) == 0:
        answer = [-1]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([2, 36, 1, 3], 1))