# q1
def q1():
    print("==========q1===========")
    WORD = []
    sorted_WORD = {}
    file_path = "Gettysburg_Address.txt"
    with open(file_path, "r")as f:
        head = f.readline()
        title = head
        for line in f:
            mystr = line.split()
            for i in range(len(mystr)):
                b = mystr[i].strip('-')
                b = b.strip(',')
                b = b.strip('.')
                if b != '':
                    WORD.append(b)
    ex_word = list(set(WORD))

    for i in range(len(ex_word)):
        if WORD.count(ex_word[i]) >= 3:
            sorted_WORD[ex_word[i]] = {WORD.count(ex_word[i])}
    print(sorted_WORD)
