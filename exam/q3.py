# q3
def q3():
    n = 0
    while n<10:
        print("나무꾼이 나무를 {}번 찍습니다".format(n+1))
        if n ==9:
            print("나무가 넘어갑니다.")
        n = n+1


if __name__ == "__main__":
    q3()