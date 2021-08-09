# p.226 확인 문제

def mul(*values):
    result = 1
    for i in values:
        result *= i
    return result
v = [5, 7, 9, 10]
print(mul(*v)) # Unpacking