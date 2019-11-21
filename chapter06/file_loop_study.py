file_path = "two_times_table.txt"
# 4개 함수 정의
#파일 읽기, 쓰기,
def file_write():
    global file_path
    f = open(file_path, "w")
    for num in range(1,6):
        format_string = "2 x {0} = {1}\n".format(num, num * 2)
        f.write(format_string)
    f.close()
    print("done - write\n")


def file_readline():
    global file_path
    f = open(file_path, "r")
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()
    f.close()
    print("done - readline\n")


def file_readlines():
    global file_path
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()
    print(lines)

    for line in lines:
        print(line, end="")
    print("done - readlines\n")


def file_for_line():
    global file_path
    f = open(file_path, "r")
    for line in f:
        print(line, end="")
    f.close()
    print("done - for_read\n")


def with_fileio():
    global file_path
    try:
        with open(file_path, "r") as f:
            for line in f:
                print(line,end="")
    except FileNotFoundError:
        print("해당 파일이 존재하지 않음",sep="\n")
    print("done - with_fileio")


def with_open():
    with open('myTextFile2.txt', 'w') as f:
        f.write('File read/write test2: line1\n')
        f.write('File read/write test2: line2\n')
        f.write('File read/write test2: line3\n')
    print("done - with_open")


def with_read():
    with open("myTextFile2.txt", 'r') as f:
        file_string = f.read()
        print(file_string)
    print("done - with_read")


if __name__ == "__main__":
    file_write()
    file_readline()
    file_readlines()
    file_for_line()
    with_fileio()
    with_open()
    with_read()
