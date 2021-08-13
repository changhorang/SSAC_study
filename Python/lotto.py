# 나의 답안
import random

l = random.sample(range(1, 46), 6)
print("이번 주 예측 로또 번호 입니다:", l)

# 1) 제일 단순
def get_lotto_v1():
    return [1, 2, 3, 4, 5, 6]

# 2) 반복문

def get_lotto_v2():
    from random import randint
    
    lotto = []
    
    while len(lotto) != 6:
        l = randint(1, 45)
        if l in lotto:
            continue
        lotto.append(l)

    return lotto

# 3) 반복문 + 집합
def get_lotto_v3():
    from random import randint

    lotto = set()
    while len(lotto) != 6:
        lotto = lotto.union({randint(1, 45)})

    return list(lotto)

# 4) random.sample()
def get_lotto_v4():
    from random import sample

    return sample(range(1, 45+1), 6)

# 5) NumPy 패키지 사용
def get_lotto_v5():
    import numpy as np

    return list(np.random.permutation(range(1, 45+1))[:6])

# 5) class
class Lotto:
    def __init__(self, n):
        self.n = n

    def make_me_rich(self):
        from random import sample

        return [sample(range(1, 45+1), 6) for _ in range(self.n)]