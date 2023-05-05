
store = [("shirt",20.00),
         ("pants",24.00),
         ("jacket",50.00),
         ("socks",5.00)]

inflation = lambda data: (data[0], data[1] + data[1] * 0.50)

inflated_prices = list(map(inflation, store))

for i in inflated_prices:
    print(i)

