def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a < b:
        answer = (b*(b + 1) - a*(a - 1))/2
    else:
        a, b = b, a
        answer = (b*(b + 1) - (a - 1)*a) /2
    return answer