def solution(s):
    try:
        int(s)
    except ValueError:
        return False
    return len(s) == 4 or len(s) == 6

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( solution("1234") )
print( solution("a234") )