def solution(s):
    for i in s:
        if int(s.count('P')) + int(s.count('p')) == int(s.count('Y')) + int(s.count('y')):
            return True
        else:
            return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( solution("pPoooyY") )
print( solution("Pyy") )