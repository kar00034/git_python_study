# # list, tuple, dictionary, set 중 하나를 선택하여 프로그램 작성
# # student_management 패키지 추가
# # 1)1. 학생목록, 2.학생추가 3.학생수정, 4.학생삭제, 5.종료메뉴
# # 2)프로그램 수행 시 먼저 student_list.txt 파일을 읽어 수행
# # 3)각각 메뉴별 수행되도록 작성
# # 4)종료시 학생목록이 student_list.txt에 저장
# # 5)프린트하여 제출
# # 6)이왕이면 2개(dictionary + 재량)
#
# # 학생 정보 : 학번, 학생명, 국어, 영어, 수학, 총점, 평균, 등수
# file_path = "student.txt"
# menu = 0
# def student_management_dic(info):
#     print("=====================================")
#     print(type(info))
#     print("=====================================")
#     for i in range(len(info)):
#         print("번호 {}".format(i + 1))
#         num = ("{}".format(i + 1))
#         keys = info[num].keys()
#         list_keys = list(keys)
#         for j in range(len(info[num])):
#             print("{} : {}".format(list_keys[j], info[num][list_keys[j]]))
#         print("=====================================")
#
#
#
# # if __name__ == "__main__":
# #     stu_list = (("01", "홍길동", "90", "90", "90"))
# #     total = 0
# #     for i in range(0,len(stu_list)):
# #         for j in range(2,5):
# #             total = total + int(stu_list[i][j])
# #     for i in range(0,len(stu_list)):
# #         student_dic = {"1": {"학번": "01", "이름": "홍길동", "국어": stu_list[i][2], "영어": stu_list[i][3], "수학": stu_list[i][4], "총점": total,
# #               "평균": total / 3}}
# #         print(student_dic)
# #     # student_management_dic(student_dic)
#
#
# def printmenu():
#     global menu
#     menu_list = ["1.학생 목록", "2.학생 추가", "3.학생 수정", "4.학생 삭제", "5.종료"]
#     print("====================================================================")
#     for i in menu_list:
#         print(i, end='\t')
#     print()
#     print("====================================================================")
#     sel_menu = input("메뉴를 선택해주세요 >> ")
#     menu = int(sel_menu)
#     try:
#         if menu == 0:
#             print("{}를 선택하셨습니다".format(menu_list[menu+10]))
#         else:
#             print("{}를 선택하셨습니다".format(menu_list[menu-1]))
#     except IndexError as e:
#         print("해당 메뉴가 없습니다.")
#     return menu
#
#
# def addstu():
#     global file_path
#     stu = ["stu_number", "name", "kor", "eng", "math"]
#     print("다음 정보를 입력해주세요.")
#     for i in range(len(stu)):
#         stu[i] = input("{} : ".format(stu[i]))
#
#     f = open(file_path, "r")
#     reading = f.read()
#     print(reading)
#
#     for i in range(0, len(stu)-1):
#         f.write(stu[i])
#     reading = f.read()
#     print(reading)
#     f.close()
#
#
# def stulist():
#     with open(file_path, "r") as f:
#         for info in f:
#             print(info)
#     pass
#
#
#
# def delstu():
#     print("del")
#
#
#
# def editstu():
#     print("edit")
#
#
# if __name__ == "__main__":
#     while True:
#         printmenu()
#         if menu == 1:
#             stulist()
#         elif menu == 2:
#             addstu()
#         elif menu == 3:
#             editstu()
#         elif menu == 4:
#             delstu()
#         elif menu == 5:
#             print("프로그램을 종료합니다.")
#             break
#         else:
#             print("다시 선택해주세요.")
#
#
# # 구상
# # list(name1,name2,name3)
# # list2(no1,no2,no3)
# #
# # dic{name1:{},name2:{},name3:{}}