tuple1 = (1, 2, 3, 4)
print("tuple1 {} type : {}".format(tuple1, type(tuple1)))
tuple2 = 5, 6, 7, 8
print("tuple2 {} type : {}".format(tuple2, type(tuple2)))
tuple3 = (9,)
tuple4 = 10,
print("tuple3 {} type : {}".format(tuple3, type(tuple3)))
print("tuple4 {} type : {}".format(tuple4, type(tuple4)))

t_list = [tuple1, tuple2, tuple3, tuple4]
print("for문")
for i in t_list:
    print("{} type : {}".format(i, type(i)))

print(tuple1[1] + tuple1.index(3))

set1 = {1, 2, 3}
set1a = {1, 2, 3, 3}
print(set1, set1a)
print(type(set1),type(set1a))