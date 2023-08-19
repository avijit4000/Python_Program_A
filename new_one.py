l=[5,6,10,11,10,9,7,20,21,18,16,10]

n=len(l)
profit=0
max_profit=0

for i in range(n):
    for j in range(i+1,n):
        if l[j]>l[i]:
            l[j]-l[i]>profit
            profit=l[j]-l[i]
            print(profit)

