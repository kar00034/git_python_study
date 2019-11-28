file_path = "lotto.txt"
num_list = []
tmp = []
find = []


def file_open():
    global num_list
    with open(file_path, "r") as f:
        head = f.readline()
        head_line = head.split()
        for i in f:
            line = i.split(',')
            tmp = [line[0], line[1], line[2], line[3], line[4], line[5], line[6].strip("\n")]
            num_list.append(tmp)


def find_num():
    global find
    for i in range(1, 46):
        cnt = 0
        for j in range(len(num_list)):
            for k in range(0, 7):
                if i == int(num_list[j][k]):
                    cnt = cnt + 1
        find.append(cnt)

    for i in range(len(find)):
        print("{} : {}".format(i + 1, find[i]))


if __name__ == "__main__":
    file_open()
    find_num()
