file_path = "coffeeShopSales.txt"
date = []
coffee_sales = []
coffee_list = []
coffee_menu = []
coffee = {}
sales = []
total_sum = []
with open(file_path, 'r') as f:
    head = f.readline()
    head_list = head.split()
    i = 0
    for line in f:
        coffee_sales = line.split()
        try:
            date.append(coffee_sales[0])
        except IndexError:
            break
        coffee[date[i]] = [{head_list[1]: coffee_sales[1]}, {head_list[2]: coffee_sales[2]},
                           {head_list[3]: coffee_sales[3]}, {head_list[4]: coffee_sales[4]}]
        i = i + 1

for i in range(len(coffee)):
    coffee_list.append(list(coffee[date[1]][i].keys()))
    coffee_menu.append(coffee_list[i][0])
print(coffee_menu)

for i in range(len(coffee)):
    print("{} : {}".format(head_list[0], date[i]), end='\t\t')
    for j in range(len((coffee_menu))):
        print("{} : {}".format(coffee_menu[j], coffee[date[i]][j][coffee_menu[j]]), end='\t ')
    total_sum.append([int(coffee[date[0]][i][coffee_menu[i]]),
                      int(coffee[date[1]][i][coffee_menu[i]]),
                      int(coffee[date[2]][i][coffee_menu[i]]),
                      int(coffee[date[3]][i][coffee_menu[i]])])
    print()

mean = len(total_sum)
for i in range(len(total_sum)):
    print("{}의 총 판매량 : {}, 하루 평균 : {}".format(coffee_list[i][0], sum(total_sum[i]), sum(total_sum[i]) / mean))