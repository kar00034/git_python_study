def add(a, b):
    return a + b


def mul(a, b):
    return a * b

if __name__ == "__main__":
    print("hello python")
    print("hi pycharm")
    a = 10
    b = 5
    print("add({}, {}) = {}\nmul({}, {}) = {}".format(a, b, add(a, b), a, b, mul(a, b)))