def solution(n):
    return list(map(int, list(str(n))[::-1]))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(solution(12345)))