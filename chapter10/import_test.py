# import_test.py
import chapter10.my_module1
import random as rnd
import datetime as dt
if __name__ == "__main__":
    print("== import_test.py ==")
else:
    print("임포")

dice1 = rnd.randint(1, 6)
dice2 = rnd.randint(1, 6)
print('주사위 2개의 숫자 : {} {}'.format(dice1, dice2))
print(rnd.randrange(0, 11, 2))

num1 = rnd.randrange(1, 10, 2)
num2 = rnd.randrange(0, 100, 10)
print('num1 : {} num2 : {}'.format(num1, num2))

menu = ['비빔밥', '된장찌개', '볶음밥', '불고기', '스파게티', '피자', '탕수육']
print(rnd.choice(menu))

print(rnd.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

test = []
test.append(1)
test.append(2)
test.append(3)

print(test[2])
test[2] = 2
if test[2] == test[1]:
    test[2] = 3

