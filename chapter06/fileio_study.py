try:
    f = open("/home/jh/PycharmProjects/git_python_study/chapter06/print_study.py", "r")
    print(f)
    data = f.read()
    print(data)
except FileNotFoundError as e:
    print("해당 파일이 존재하지 않음", e, sep='\n')
finally:
    print("finally - done")
    f.close()

try:
    f = open("/home/jh/PycharmProjects/git_python_study/chapter06/test.txt", "x")
    f.write(data)
except FileExistsError as e:
    f = open("/home/jh/PycharmProjects/git_python_study/chapter06/test.txt", "w")
    f.write(data)
    print("해당 파일이 존재합니다", e, sep='\n')
finally:
    f.close()
    print("finally - done")


print("done")