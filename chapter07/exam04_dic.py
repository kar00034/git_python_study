# 학생 정보 : 학번, 학생명, 국어, 영어, 수학, 총점, 평균
file_path = "student.txt"
menu = 0
sdic = {}
slist = []
list_keys = []

def find_key():
    global sdic
    global list_keys
    key = sdic.keys()
    list_keys = list(key)


def read_file():
    global sdic
    global list_keys
    i = 0
    try:
        f = open("student.txt", "r")
        line = f.readline()
        while line:
            line_dic = line.split()
            slist.append(line_dic)
            sdic[slist[i][0]]=[slist[i][1], slist[i][2], slist[i][3], slist[i][4]]
            line = f.readline()
            i = i+1
    except FileNotFoundError as er:
        print("파일이 없습니다.", er, sep='\n')
    finally:
        f.close()
        find_key()



def printmenu():
    global menu
    menu_list = ["1.학생 목록", "2.학생 추가", "3.학생 수정", "4.학생 삭제", "5.종료"]
    print("====================================================================")
    for i in menu_list:
        print(i, end='\t')
    print()
    print("====================================================================")
    sel_menu = input("메뉴를 선택해주세요 >> ")
    menu = int(sel_menu)
    try:
        if menu == 0:
            print("{}를 선택하셨습니다".format(menu_list[menu + 10]))
        else:
            print("{}를 선택하셨습니다".format(menu_list[menu - 1]))
    except IndexError as e:
        print("해당 메뉴가 없습니다.")
    return menu


def stulist():
    global list_keys
    global sdic

    print("학생번호\t이름\t\tkor\teng\tmath\t총점\t\t평균")
    for i in range(len(sdic)):
        total = int(sdic[list_keys[i]][1])+int(sdic[list_keys[i]][2])+int(sdic[list_keys[i]][3])
        avg = total/3
        print("{:}\t{:>8}\t{}\t{}\t{}\t\t{}\t\t{:.2f}".format(list_keys[i], sdic[list_keys[i]][0], sdic[list_keys[i]][1], sdic[list_keys[i]][2], sdic[list_keys[i]][3], total, avg))


def addstu():
    cnt = 0
    global sdic
    global list_keys
    print("현재 있는 학생 번호 : {}".format(list_keys))
    add_list = ["학번", "이름", "kor", "eng", "math"]
    print("다음 정보를 입력하세요.")
    for i in range(0, len(add_list)): #입력
        add_list[i] = input("{} : ".format(add_list[i]))
    for i in range(len(sdic)): #확인
        print(sdic[list_keys[i]][0])
        print(add_list[0][0])
        if add_list[0][0] == list_keys[i]:
            print("중복입니다. 다시 입력해주세요")
            cnt = 1
            break
    if cnt != 1: #중복 아닐시
        sdic[add_list[0]]= [add_list[1],add_list[2],add_list[3],add_list[4]]
        print("입력되었습니다.")
        find_key()


def editstu():
    global sdic
    global list_keys
    cnt = 1
    for i in range(len(sdic)):
        for j in range(len(list_keys[i])):
            print(list_keys[i],sdic[list_keys[i]], end='\t')
        print()
    tar = input("수정할 학생의 번호를 입력하세요 > ")
    for i in range(len((sdic))):
        if tar == list_keys[i]:
            edit_list = ["이름", "kor", "eng", "math"]
            print("다음 정보를 입력하세요.")
            for j in range(0, len(edit_list)):
                sdic[list_keys[i]][j] = input("{} : ".format(edit_list[j]))
                cnt = 0
            break
    if cnt == 1:
        print("해당학생은 없습니다.")


def delstu():
    global sdic
    global list_keys
    cnt = 1
    for i in range(len(sdic)):
        for j in range(len(list_keys[i])):
            print(list_keys[i],sdic[list_keys[i]], end='\t')
        print()
    tar = input("삭제할 학생의 번호를 입력하세요 > ")
    for i in range(len((sdic))):
        if tar == list_keys[i]:
            print(sdic[list_keys[i]])
            ans = input("삭제하려면 y을 눌러주세요")
            if ans == 'y':
                del sdic[list_keys[i]]
                print("삭제되었습니다.")
                cnt = 0
                break
            else:
                print("취소되었습니다.")
                cnt = 0
                break
    find_key()
    if cnt == 1:
        print("해당학생은 없습니다.")


def save():
    global sdic
    global list_keys
    with open(file_path, "w")as f:
        for i in range(len((list_keys))):
            f.write(list_keys[i] + '\t' + sdic[list_keys[i]][0] +
                    '\t' + sdic[list_keys[i]][1] + '\t' + sdic[list_keys[i]][2] +
                    '\t' + sdic[list_keys[i]][3] + '\n')
    print("프로그램을 종료합니다.")



if __name__ == "__main__":
    read_file()
    while True:
        printmenu()
        if menu == 1:
            stulist()
        elif menu == 2:
            addstu()
        elif menu == 3:
            editstu()
        elif menu == 4:
            delstu()
        elif menu == 5:
            save()
            break
        else:
            print("다시 선택해주세요.")
