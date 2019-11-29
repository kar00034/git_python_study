# q4
import random as rnd
import numpy as np


def solution(array,commands):
    answer = [array,commands]

    print("array = {}\ncommands =\n{}".format(answer[0],answer[1]))

    return answer


def bubble_sort(target):
    for i in range(0, len(target)-1):
        for j in range(0, len(target)-1-i):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
    return target


def q4(i,j,k):
    rnd.seed(1)
    array = []
    target = []
    while len(array) < 15:
        array.append(rnd.randint(1, 100))
    commands = np.array(array).reshape(5, 3)

    for a in range(len(array)):
        if a >= i:
            target.append(array[a])
            if a >= j:
                break
    sorted_target = bubble_sort(target)

    solution(array,commands)
    print("array의 {}번째에서 {}번째의 숫자는 {}입니다.".format(i, j, target))
    print("정렬 : {}".format(sorted_target))
    print("정렬 후 {}번째의 숫자는 {}입니다".format(k,target[k-1]))


if __name__ == "__main__":
    q4(3,7,2)
