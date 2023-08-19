import pandas as pd

df=pd.read_csv("D:\Pyn\MSDSM\SEMESTER_1\Programing\BSE Sensex Daily Close Jan1990 Oct2020.csv")
df_1=df['Close']
price=[]
for i in df_1:
    price.append(i)


def stock(price,n):
    if (n==1):
        return
    i=0
    while (i<(n-1)):
        while ((i<n-1) and (price[i+1]<=price[i])):
            i+=1
        if (i==n-1):
            break
        buy=i
        i+=1
        while((i<n) and (price[i]>=price[i-1])):
            i+=1
            sell=i-1
            print("Buy on day:",buy, "\t",
              "sell on day: ", sell)
n = len(price)
stock(price, n)