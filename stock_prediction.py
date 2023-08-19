# Python3 program for the above approach
def max_profit(prices: list, days: int) -> int:
	profit = 0
	for i in range(1, days):
		if prices[i] > prices[i-1]:
			profit += prices[i] - prices[i-1]
	return profit
if __name__ == '__main__':
	# stock prices on consecutive days
	prices = [5,6,10,11,10,9,7,20,21,18,16,10]
	# function call
	profit = max_profit(prices, len(prices))
	print(profit)


