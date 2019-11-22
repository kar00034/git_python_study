# list, tuple, dictionary, set 중 하나를 선택하여 프로그램 작성
# student_management 패키지 추가
# 1)1. 학생목록, 2.학생추가 3.학생수정, 4.학생삭제, 5.종료메뉴
# 2)프로그램 수행 시 먼저 student_list.txt 파일을 읽어 수행
# 3)각각 메뉴별 수행되도록 작성
# 4)종료시 학생목록이 student_list.txt에 저장
# 5)프린트하여 제출
# 6)이왕이면 2개(dictionary + 재량)

# 학생 정보 : 학번, 학생명, 국어, 영어, 수학, 총점, 평균
file_path = "student.txt"
menu = 0
slist = []


def read_file():
    global slist
    try:
        f = open("student.txt", "r")
        line = f.readline()
        while line:
            line_list = line.split()
            slist.append(line_list)
            line = f.readline()
    except FileNotFoundError as er:
        print("파일이 없습니다.", er, sep='\n')
    finally:
        f.close()


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
    global slist
    print("학생번호\t이름\tkor\teng\tmath\t총점\t\t평균")
    for i in range(len(slist)):
        total = int(slist[i][2]) + int(slist[i][3]) + int(slist[i][4])
        avg = total / 3
        print("{}\t{}\t{}\t{}\t{}\t\t{}\t\t{:.2f}".format(slist[i][0], slist[i][1], slist[i][2], slist[i][3],
                                                            slist[i][4], total, avg))


def addstu():
    cnt = 0
    global slist
    add_list = ["학번", "이름", "kor", "eng", "math"]
    print("다음 정보를 입력하세요.")
    for i in range(0, len(add_list)):
        add_list[i] = input("{} : ".format(add_list[i]))
    for i in range(len(slist)):
        if add_list[0] == slist[i][0]:
            print("중복입니다. 다시 입력해주세요")
            cnt = 1
            break
    if cnt != 1:
        slist.append(add_list)
        print("입력되었습니다.")


def editstu():
    global slist
    cnt = 1
    print("학생번호\t이름\tkor\teng\tmath")
    for i in range(len(slist)):
        for j in range(len(slist[i])):
            print(slist[i][j],end='\t')
        print()
    tar = input("수정할 학생의 번호를 입력하세요 > ")
    for i in range(len((slist))):
        if tar == slist[i][0]:
            edit_list = ["이름", "kor", "eng", "math"]
            print("다음 정보를 입력하세요.")
            for j in range(0, len(edit_list)):
                slist[i][j+1] = input("{} : ".format(edit_list[j]))
                cnt = 0
            break
    if cnt == 1:
        print("해당학생은 없습니다.")


def delstu():
    global slist
    cnt = 0
    print("학생번호\t이름\tkor\teng\tmath")
    for i in range(len(slist)):
        for j in range(len(slist[i])):
            print(slist[i][j],end='\t')
        print()
    tar = input("삭제할 학생의 번호를 입력하세요 > ")
    for i in range(len(slist)):
       if tar == slist[i][0]:
           ans = input("삭제하려면 y을 눌러주세요")
           if ans == 'y':
               del slist[i]
               print("삭제되었습니다.")
               break
           else:
               print("취소되었습니다.")
               break
           cnt = 0
    if cnt != 1:
        print("해당 학생은 없습니다.")



def save():
    global slist
    with open(file_path, "w")as f:
        for i in range(len((slist))):
            f.write(slist[i][0] + '\t' + slist[i][1] + '\t' + slist[i][2] + '\t' +
                    slist[i][3] + '\t' + slist[i][4] + '\n')
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
