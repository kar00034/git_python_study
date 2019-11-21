print("test", "test1", sep=",")
print("%s, %d"%('test', 10)) #2개 이상일 경우 괄호로 묶음
a = 0.123456789
print("{0:.2f}, {0:.5f}".format(a))

print("{:2d}".format(3))
print("{:02d}".format(3))
print("{:>5d}".format(3))
print("{:<5d}".format(3))
print("{:.3f}".format(3))
print("{:,}".format(1234567))
print("{:.1%}".format(0.3258))
print("{:.2e}".format(92500000000))
print("16진수 : {0:x} \t8진수 : {0:o} \t2진수 : {0:b}\t10진수 : {0}".format(16))

