def maxProfit(price, start, end):
    if (end <= start):
        return 0
    profit = 0
    for i in range(start, end, 1):
        for j in range(i+1, end+1):
            if (price[j] > price[i]):
                curr_profit = price[j] - price[i] + maxProfit(price, j + 1, end)
                              # + maxProfit(price, start, i - 1) +

                profit = max(profit, curr_profit)
    return profit
price =[5,6,10,11,10,9,7,20,21,18,16,10]
n = len(price)
print(maxProfit(price, 0, n - 1))
