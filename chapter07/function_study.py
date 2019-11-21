# 1.리스트 전달 2. 투플 3. dictionary
def my_student_info_list(info):
    print("==================")
    print(type(info))
    for i in range(len(info)):
        print("name = {}".format(info[i][0]))
        print("ID = {}".format(info[i][1]))
        print("phoneNumber = {}".format(info[i][2]))


def my_student_info_tuple(info):
    print("==================")
    stu_tuple = (info,)
    print(type(stu_tuple))
    for i in range(len(stu_tuple)):
        for j in range(len(stu_tuple[i])):
            print("name = {}".format(stu_tuple[i][j][0]))
            print("ID = {}".format(stu_tuple[i][j][1]))
            print("phoneNumber = {}".format(stu_tuple[i][j][2]))


def my_student_info_dictionary(info):
    j = 0
    print("===================")
    print(type(info))
    for i in range(len(info)):
        print("번호 {}".format(i+1))
        num = ("{}".format(i+1))
        keys = info[num].keys()
        list_keys = list(keys)
        for j in range(len(info[num])):
             print("{} : {}".format(list_keys[j], info[num][list_keys[j]]))



if __name__ == "__main__":
    std_list = [["현아", "01", "01-235-6789"], ["진수", "02", "01-987-6543"]]
    # std_tuple = (("현아", "01", "01-235-6789"), ("진수", "02", "01-987-6543"))
    std_dic = {"1":{"학생이름" : "현아","전화번호" : "01-235-6789"}, "2" : {"학생이름" : "진수", "전화번호" : "01-987-6543"}}
    my_student_info_list(std_list)
    my_student_info_tuple(std_list)
    my_student_info_dictionary(std_dic)

    # print("=============================")
    # print(type(std_list), std_list)
    # print(type(std_tuple), std_tuple)
    # print(type(std_dic), std_dic)
