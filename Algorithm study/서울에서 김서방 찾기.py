def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 {}에 있다".format(i)
    return answer

# 실행을 위한 테스트코드입니다.
print(solution(["Queen", "Tod", "Kim"]))