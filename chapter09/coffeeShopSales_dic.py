file_path = "coffeeShopSales.txt"
date = []
coffee = {}
coffee_sales = []
coffee_list = []
coffee_menu = []

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

for i in range(len((coffee_list))):
    coffee_menu.append(coffee_list[i][0])

for i in range(len(coffee)):
    print("{} : {}".format(head_list[0], date[i]), end='\t\t')
    for j in range(len((coffee_menu))):
        print("{} : {}".format(coffee_menu[j], coffee[date[i]][j][coffee_menu[j]]), end='\t ')
    print()

