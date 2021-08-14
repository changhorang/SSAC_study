def solution(arr1, arr2):
    answer = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))] for i in range(len(arr1))]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([[1,2], [2,3]], [[3,4],[5,6]]))
print(solution([[1,2,3], [2,3,4]], [[3,4,5],[5,6,7]]))