# 로또번호생성기 작성, 당첨번호에 따라 순위를 구하는 프로그램 작성 6 5+n 4 3
# 5천원치 로또번호 생성
import random as rnd
from chapter04.exam02 import bubble_sort


def lotto_generator():
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(rnd.randint(1, 45))
    return lotto_num


def lotto_start(a, b, c, d, e, f):
    sorted_lotto = bubble_sort(list(lotto_generator()))
    # sorted_lotto.append(rnd.randint(1,46))
    bonus = rnd.randint(1, 45)
    print("수정 전 보너스번호 : {}".format(bonus))
    while sorted_lotto.count(bonus) == 1:
        bonus = rnd.randint(1, 45)
    print("로또 번호 : {}".format(sorted_lotto))  # 정렬된 결과
    print("최종 보너스 번호 : {}".format(bonus))

    mylist = {a, b, c, d, e, f}
    cnt = 0
    bon = 0
    for i in sorted_lotto:
        for j in mylist:
            if j == i:
                cnt = cnt + 1
    for i in mylist:
        if bonus == i:
            bon = 1

    if cnt == 6:
        print("1등입니다 축하합니다")
    elif cnt == 5:
        if bon == 1:
            print("2등입니다.")
        else:
            print("3등입니다.")
    elif cnt == 4:
        print("4등입니다.")
    elif cnt == 3:
        print("5등입니다.")
    else:
        print("꽝입니다.")
    print("{} {}".format(cnt,bon))


if __name__ == "__main__":
    # rnd.seed(1)
    lotto_start(5,8,9,17,32,29)

