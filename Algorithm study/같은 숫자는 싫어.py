def solution(arr):
    answer = []
    for i in arr:
        if (len(answer) == 0) or answer[-1] != i:
            answer.append(i)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("133303"))