import random as rnd


def bubble_sort(random_list):
    print(random_list)


if __name__ == "__main__":
    random_list = []
    rnd.seed(1)
    for num in range(0, 10):
        random_list.append(rnd.randint(1, 46))
    print(random_list)

    sorted_list = bubble_sort(random_list)
    print("정렬된 결과\n{}".format(sorted_list))

    i = 0
    j = 0

    for i in random_list:
        for j in random_list:
            if random_list(j) < random_list(j+1):
                tmp = random_list(j)
