def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


if __name__ == "__main__":
    print("hello python")
    print("hi pycharm")
    a = 10
    b = 5
    print("add({}, {}) = {}".format(a, b, add(a, b)))
    print("mul({}, {}) = {}".format(a, b, mul(a, b)))
    print("div({}, {}) = {}".format(a, b, div(a, b)))