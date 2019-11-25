scores = [90, 80, 95, 85]


def score():
    score_sum = 0
    subject_num = 0
    for score in scores:
        score_sum = score_sum + score
        subject_num = subject_num + 1

    avg = score_sum / subject_num
    print("총점 : {}  평균 : {}".format(score_sum, avg))


if __name__ == "__main__":
    tlist = [1, 2, 3, 4, 5]
    res = (lambda x: x ** 2)(3)
    print(res)

    mySquare = lambda x: print(x ** 2)
    mySquare(3)
    score()

    for i in range(len(tlist)):
        # print(tlist[i]**2)
        if tlist[i] % 2 != 0:
            print("홀수 : {}".format(tlist[i] ** 2))
