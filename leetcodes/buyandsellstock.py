def buyandsellstock (prices):
    minpricesofar = float('inf')
    maxprofit = 0.0
    for price in prices:
        maxprofittoday = price - minpricesofar
        maxprofit = max(maxprofit, maxprofittoday)
        minpricesofar = min(minpricesofar, price)
    return maxprofit
A = [310, 315, 275,295, 260, 270, 290,230, 255, 250]
print(buyandsellstock(A))
def longestsubArray(A):
    A.sort()
    maxsubelement = 0
    count = 1
    currentvalue = 0
    for i in range (1, len(A)):
        if A[currentvalue] != A[i]:
            maxsubelement = max(maxsubelement, i - currentvalue)
            currentvalue = i
    return maxsubelement
B= [1,2,2,2,3,4,4,4,3,3,5,5,6,6,6]
print(longestsubArray(B))
print(B)

def buy_sell_stock_twice(prices):
    max_total_profix = 0.0
    min_price_so_far = float('inf')
    first_buy_sell_profix = [0.0] *len(A)
    for i , price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profix = max(max_total_profix, price - min_price_so_far)
        first_buy_sell_profix[i] = max_total_profix
    
    max_price_so_far =float('-inf')
    for i , price in reversed(list(enumerate(prices[1:],1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profix = max(max_total_profix, max_price_so_far - price + first_buy_sell_profix[i-1])
    return max_total_profix


C = [12, 11, 13, 9, 12, 8, 14, 13, 15]
print(buy_sell_stock_twice(C))

def buy_sell_stock_twice2(prices):
    max_total_profix = 0.0
    min_price_so_far = float('inf')   
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profix = max(max_total_profix, price-min_price_so_far)
    
    max_price_so_far = float('-inf')
    max_total_profix2 = max_total_profix
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profix2 = max(max_total_profix2, max_total_profix2 - price + max_total_profix)
    return max_total_profix2
        
C = [12, 11, 13, 9, 12, 8, 14, 13, 15]
print(buy_sell_stock_twice2(C))  
    

