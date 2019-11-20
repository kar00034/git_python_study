import random as rnd
#left = list[0], right = list[-1]
#mid = (left + right)/2
#if i > mid -> mid> num 버림
#if right<left 종료
from chapter04.exam02 import bubble_sort
def binary_search_value(target):
    print("binary_search_value")
    i=50
    j=101
    list = [i for i in range(i, j)]
    left = list[0]
    right = list[-1]
    mid = (left+right)//2

    cnt = 1
    if i > target or j < target:
        print("해당하는 수는 없습니다")
    else:
        while True:
            mid = (left + right) // 2
            print(left, mid, right)
            if target > mid:
                left = mid
                cnt = cnt + 1
            elif target < mid:
                right = mid
                cnt = cnt + 1
            else:
                print("검색 : {}번 \n".format(cnt))
                break


def binary_search_index(target):
    print("binary_search_index\nindex,value")
    setlist = set()
    # rnd.seed(2)
    while len(setlist)<21:
        setlist.add(rnd.randint(1, 200))
    print("정렬전\n{}".format(setlist))
    left = 0
    right = len(setlist)-1
    cnt = 0
    sorted_list = bubble_sort(list(setlist))
    print("정렬후\n{}".format(sorted_list))

    while True:
        mid = (left+right)//2
        print("left : {}  {}\t\tmid : {:2}  {}\t\tright : {}  {}\t\t target : {}".format(left, sorted_list[left], mid, sorted_list[mid], right, sorted_list[right], target))
        if target > sorted_list[mid]:
            left = mid +1
            cnt = cnt + 1
        elif target < sorted_list[mid]:
            right = mid - 1
            cnt = cnt + 1
        else:
            print("검색 : {}\n위치 : {}번".format(cnt, mid))
            break

        if left >= right:
            print("{}번 검색했지만 해당하는 수는 없습니다.".format(cnt))
            break






# binary_search_value(51)
binary_search_index(100)