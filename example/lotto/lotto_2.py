import random

count = 10
for i in range(0, count):
    lotto = random.sample(range(1, 46), 6)
    if sum(lotto) > 138:
        lotto.sort()
        print(i + 1, "게임 : ", lotto)
