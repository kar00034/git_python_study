# dic로 전환 {날자 = key, menu = key}
file_path = "coffeeShopSales.txt"
coffee = []
espresso = []
americano = []
cafelatte = []
cappucino = []


with open(file_path, 'r') as f:
    head = f.readline()
    head_list = head.split()

    for line in f:
        coffee = line.split()
        espresso.append(int(coffee[1]))
        americano.append(int(coffee[2]))
        cafelatte.append(int(coffee[3]))
        cappucino.append(int(coffee[4]))

total_sum = [sum(espresso), sum(americano), sum(cafelatte), sum(cappucino)]
total_mean = [sum(espresso)/len(espresso), sum(americano)/len(americano), sum(cafelatte)/len(cafelatte), sum(cappucino)/len(cappucino)]

for k in range(len(total_sum)):
    print("[{}] 판매량".format(head_list[k+1]))
    print("나흘 전체: {}, 하루 평균 : {}\n".format(total_sum[k], total_mean[k]))
