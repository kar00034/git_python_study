def string_split():
    coffee_menu = "에스프레소 아메리카노 카페라떼 카푸치노"
    print(type(coffee_menu.split()), coffee_menu.split())
    coffee_list = coffee_menu.split()
    [print(coffee) for coffee in coffee_list]

    coffee_menu2 = "에스프레소,아메리카노,카페라떼,카푸치노"
    [print(type(coffee), coffee) for coffee in coffee_menu2.split(',')]
    coffee_menu3 = "에스프레소\n아메리카노\n카페라떼\n카푸치노"
    [print(coffee) for coffee in coffee_menu3.split()]
    print()
    [print(coffee) for coffee in coffee_menu2.split(',', 2)]
    python_str04 = '+82-01-2345-6789'
    print(python_str04.split('-', 1))


def string_strip():
    python_str01 = '  python  '
    python_str02 = 'aaapythonaaa'
    python_str03 = 'aaabbbpythonbbbaaa'
    python_str04 = 'aaaballaaa'
    python_str05 = '\n This is very \nfast.\n\n'

    print(python_str01.strip())
    print(python_str02.strip('a'))
    print(python_str03.strip('ba'))
    print(python_str04.strip('a'))  #중간 a는 제거 불가능
    print(python_str05.strip())     #중간 \n 제거 불가능


def string_find():
    str_f = "python code."
    print("찾는 문자열 위치 : ", str_f.find('python'))
    print("찾는 문자열 위치 : ", str_f.find('code'))
    print("찾는 문자열 위치 : ", str_f.find('n'))
    print("찾는 문자열 위치 : ", str_f.find('easy'))
    print("찾는 문자열 위치(0~5) : ", str_f.find('python', 0, 5))
    print("찾는 문자열 위치(0~8) : ", str_f.find('python', 0, 8))
    print("o의 갯수 : ", str_f.count('o'))
    
    str_c = "python is powerful. python is easy to learn. python is open."
    print("python의 갯수는? :", str_c.count('python'))
    print("powerful의 갯수는? :", str_c.count('powerful'))
    print("ipython의 갯수는? :", str_c.count('ipython'))

    str_se = "python is powerful. python is easy to learn"
    print("python으로 시작? :", str_se.startswith("python"))
    print("is로 시작? :", str_se.startswith("is"))
    print(".으로 시작? :", str_se.startswith("."))
    print("learn으로 시작? :", str_se.startswith("learn"))


def string_replace():
    str_a = 'python is fast. python is freindly. python is open.'
    print(str_a)
    print(str_a.replace('python', 'ipython'))
    print(str_a.replace('python', 'ipython', 2))

    str_b = '[python] [is] [fast]'
    str_b1 = str_b.replace('[', '')
    str_b2 = str_b.replace(']', '')
    str_b3 = str_b.replace('[', '')
    str_b3 = str_b3.replace(']', '')

    print(str_b)
    print(str_b1)
    print(str_b2)
    print(str_b3)


if __name__ == "__main__":
    string_split()
    string_strip()
    string_find()
    string_replace()
