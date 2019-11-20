for i in [0, 1, 2, 3, 4, 5]:
    print(i, end=' ')

print()

for i in range(1, 10):
    print(i, end=' ')

print()

for i in range(0, 10, 2):
    print(i, end=' ')

print()

print("{}\n{}".format(range(0, 10), list(range(0, 10))))
print("{}".format(range(10)))

print(list(range(0, 20, 5)))
print(list(range(-10, 0, 2)))
print(list(range(3, -10, -3)))
print(list(range(0, -5, 1)))


# 구구단
# gugu(2) = 2단   gugudan() 전체 구구단
# gugudan_land()
# 2*1 = 2 3*1 = 3 4*1 =4
# 2*2 3*2 4*2
def gugu(num):
    print("gugudan{}".format(num))
    for i in range(1, 10):
        print("{} * {} = {}".format(num, i, num * i), end='\t')
    print()
    print()


def gugudan():
    print("gugudan")
    for i in range(2, 10):
        for j in range(1, 10):
            print("{0} * {1} = {2:2}".format(i, j, i * j), end='\t')
        print()
    print()
    print()


def gugudan_land():
    print("gugudan_land")
    for i in range(1, 10):
        for j in range(2, 10):
            print("{0} * {1} = {2:2}".format(j, i, i * j), end='\t')
        print()


# gugu(9)
# gugudan()
# gugudan_land()


names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95, 96, 97, 94]

for name, score in zip(names, scores):
    print(name, score)
print()

numbers = [1,2,3,4,5]
square = [i**2 for i in numbers]
print(square)
square = [i**2 for i in numbers if i < 4]
print(square)
square = [i**2 for i in range(1, 6) if i >= 3]
print(square)
