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
        