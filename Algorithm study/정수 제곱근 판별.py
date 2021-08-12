import math

def solution(n):
    answer = 0
    i = [i for i in range(int(math.sqrt(n) + 1))]
    if math.sqrt(n) in i:
        answer = (math.sqrt(n) + 1)**2
    else:
        answer = -1
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(solution(121)))
print("결과 : {}".format(solution(3)))