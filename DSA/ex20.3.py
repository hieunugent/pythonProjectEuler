stock =[10,7,2,5,9,11,8,15]
# we know the first price is must be the min and max price possible
# which we only buy not sell any
# we can only sell second day if previous day is low price
# continuos price increase will give max price
# 
def trade(prices):
    price =[0]
    min_value = float('inf')
    min_index =-1
    max_value = float('-inf')
    max_index =-1
  
print(trade(stock))
