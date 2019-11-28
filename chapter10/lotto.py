# 로또번호생성기 작성, 당첨번호에 따라 순위를 구하는 프로그램 작성 6 5+n 4 3
# 5천원치 로또번호 생성
import random as rnd
from chapter04.exam02 import bubble_sort


def lotto_generator():
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(rnd.randint(1, 45))
    return lotto_num


def lotto_start():
    mylist1 = set()
    mylist2 = set()
    mylist3 = set()
    mylist4 = set()
    mylist5 = set()
    while len(mylist1) < 6:
        mylist1.add(rnd.randint(1, 45))
        mylist2.add(rnd.randint(1, 45))
        mylist3.add(rnd.randint(1, 45))
        mylist4.add(rnd.randint(1, 45))
        mylist5.add(rnd.randint(1, 45))

    sorted_mylist = [bubble_sort(list(mylist1)), bubble_sort(list(mylist2)), bubble_sort(list(mylist3)), bubble_sort(list(mylist4)),
                     bubble_sort(list(mylist5))]

    print("내 로또 번호")
    for i in range(len(sorted_mylist)):
        print("{}".format(sorted_mylist[i]))
    sorted_lotto = bubble_sort(list(lotto_generator()))
    # sorted_lotto.append(rnd.randint(1,46))
    bonus = rnd.randint(1, 45)
    while sorted_lotto.count(bonus) == 1:
        bonus = rnd.randint(1, 45)
    print("로또 번호 : {}".format(sorted_lotto))  # 정렬된 결과
    print("보너스 번호 : {}".format(bonus))

    cnt = []
    # print(sorted_mylist)
    for i in range(len(sorted_mylist)):
        bon = 0
        cnt_num = 0
        for j in range(len(mylist1)-1):
            if sorted_mylist[i][j] == sorted_lotto[j]:
                cnt_num = cnt_num + 1
            if sorted_mylist[i][j] == bonus:
                bon = 1
        cnt.append(cnt_num)
        print("복권 {} : {} + {}개 일치".format(i+1, cnt_num, bon))
        if cnt_num == 6:
            print("1등입니다 축하합니다")
        elif cnt_num == 5:
            if bon == 1:
                print("2등입니다.")
            else:
                print("3등입니다.")
        elif cnt_num == 4:
            print("4등입니다.")
        elif cnt_num == 3:
            print("5등입니다.")
        else:
            print("꽝입니다.")




if __name__ == "__main__":
    # rnd.seed(5)
    lotto_start()
