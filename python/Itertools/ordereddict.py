from collections import OrderedDict
product_dict = OrderedDict()
for i in range(int(input())):
    name, space, price = input().rpartition(" ")
    product_dict[name] = product_dict.get(name, 0) + int(price)
#print(product_dict)
for item, price in product_dict.items():
    print(item, price)