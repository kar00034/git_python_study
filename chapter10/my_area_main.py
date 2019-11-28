from chapter10.my_area import *  # from 패키지명 import 함수(변수)이름

import chapter10.my_area
# print('pi = ', PI)
from chapter10.my_module1 import *
from chapter10.my_module2 import *

print("square area = ", square_area(5))
print(dir(chapter10.my_area))
[print(content) for content in dir(chapter10.my_area)]

fun1()
fun2()
fun3()