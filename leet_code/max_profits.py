def max_profit(prices: list) -> int:
    p1 = 0
    p2 = 1
    
    max_profit = []
    for i in range(len(prices) - 1):
        if prices[p1] < prices[p2]:
            max_profit.append(prices[p2] - prices[p1])
        p1 += 1
        p2 += 1
    
    return sum(max_profit)

def main() -> None:
                #1 2 3 4 5 6 
    price_one = [7,1,5,3,6,4]
    price_two = [1,2,3,4,5]
    price_three = [7,6,4,3,1]
    for price_array in [price_one, price_two, price_three]:
        print(max_profit(price_array))
    
if __name__ == '__main__':
    main()