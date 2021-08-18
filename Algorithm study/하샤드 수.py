# 더 좋은 풀이
def solution(x):
    answer = True
    a = str(x)
    b = 0
    for i in range(len(a)):
        b += int(a[i])
    if x % b != 0:
        answer = False 
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(18))

# 나의 풀이
# def solution(x):
#     answer = True
#     a = []
#     b = str(x)
#     c = 0
#     for i in range(len(b)):
#         a.append(b[i])
#     for j in range(len(a)):
#         c += int(a[j])
#     if x % c != 0:
#         answer = False 
#     return answer
