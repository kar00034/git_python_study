import random as rnd
import numpy as np


def bubble_sort(target):
    for i in range(0, len(target) - 1):
        for j in range(0, len(target) - 1 - i):
            if target[j] > target[j + 1]:
                target[j], target[j + 1] = target[j + 1], target[j]
    return target


# q1##################################################################################
def q1():
    print("======================q1======================")
    WORD = []
    sorted_WORD = {}
    file_path = "Gettysburg_Address.txt"
    with open(file_path, "r")as f:
        head = f.readline()
        for line in f:
            mystr = line.split()
            for i in range(len(mystr)):
                b = mystr[i].strip(',.-')
                if b != '':
                    WORD.append(b)
    ex_word = list(set(WORD))

    for i in range(len(ex_word)):
        if WORD.count(ex_word[i]) >= 3:
            sorted_WORD[ex_word[i]] = WORD.count(ex_word[i])
    sorted_val = sorted(sorted_WORD.items(), key=lambda t: t[1], reverse=True)

    for i in range(len(sorted_val)):
        print("{} : {}".format(sorted_val[i][0], sorted_val[i][1]))


# q2#################################################################################

def q2(a, b, c):
    print("{} {} {} 의 값 : ".format(a, c, b), end='\t')
    if c == '+':
        res = lambda a, b: a + b
    elif c == '-':
        res = lambda a, b: a - b
    elif c == '*':
        res = lambda a, b: a * b
    elif c == '/':
        res = lambda a, b: a / b
    print(res(a, b))


# q3##################################################################################
def q3():
    print("======================q3======================")
    n = 0
    while n < 10:
        print("나무꾼이 나무를 {}번 찍습니다".format(n + 1))
        if n == 9:
            print("나무가 넘어갑니다.")
        n = n + 1


# q4#################################################################################
def solution(array,commands):
    print("======================q4======================")
    ans = [[], [], []]
    print(array)
    for i in range(len(commands)):
        target = array[commands[i][0] - 1:commands[i][1]]
        sort_target = bubble_sort(target)
        ans[i] = list(sort_target)
        print("array의 {}번부터 {}번은 {}입니다. 그 중 {}번째는 {}입니다  ".format(commands[i][0], commands[i][1], target,
                                                                      commands[i][2], ans[i][commands[i][2] - 1]))


# main#################################################################################
if __name__ == "__main__":
    q1()
    # print()
    # print("======================q2======================")
    # q2(30,10,'+')
    # q2(30, 10, '-')
    # q2(30, 10, '*')
    # q2(30, 10, '/')
    # print()
    # q3()
    # print()
    # array = [1, 5, 2, 6, 3, 7, 4]
    # commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    # solution(array,commands)
