# q2
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


if __name__ == "__main__":
    q2(30,10,'/')