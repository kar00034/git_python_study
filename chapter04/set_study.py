# 로또번호생성기 작성, 당첨번호에 따라 순위를 구하는 프로그램 작성 6 5+n 4 3
# 5천원치 로또번호 생성
import random as rnd
from chapter04.exam02 import bubble_sort


def lotto_generator():
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(rnd.randint(1, 46))
    return lotto_num


if __name__ == "__main__":
    rnd.seed()

    sorted_lotto = bubble_sort(list(lotto_generator()))
    # sorted_lotto.append(rnd.randint(1,46))

    print("로또 번호 : {}".format(sorted_lotto)) # 정렬된 결과