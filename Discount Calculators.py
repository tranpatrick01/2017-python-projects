price = int(input("Origional price: "))
dis = int(input("Discount %: " ))  


def cal(org,disounts):
    a = disounts/100
    b = org * a
    print('After: ' + str(b))
    print('You save: ' + str(price-b))
cal(price,dis)