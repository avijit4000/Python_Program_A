import pandas as pd

df=pd.read_csv("D:\Pyn\MSDSM\SEMESTER_1\Programing\BSE Sensex Daily Close Jan1990 Oct2020.csv")
df_1=df['Close']
prices=[]
for i in df_1:
    prices.append(i)

def max_profit(prices: list, days: int) -> int:
	profit = 0
	for i in range(1, days): # checks if elements are adjacent and in increasing order
		if prices[i] > prices[i-1]: # difference added to 'profit'
			profit += prices[i] - prices[i-1]
	return profit
# prices=[5,6,10,11,10,9,7,20,21,18,16,10]

profit = max_profit(prices, len(prices))
print(profit)