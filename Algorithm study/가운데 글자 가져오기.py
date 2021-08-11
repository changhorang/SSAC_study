def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        answer = s[int((len(s))/2 - 1):int(len(s)/2 + 1)]
    else:
        answer = s[int((len(s) - 1)/2)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("power"))