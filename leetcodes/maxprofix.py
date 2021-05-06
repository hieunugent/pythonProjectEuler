def maxProfit(self, prices: List[int]) -> int:
    maxprofix = 0
    minprice = prices[0]
    for i in range(1, len(prices)):
            if minprice > prices[i]:
                minprice = prices[i]
            else:
                temp = prices[i]-minprice
                if temp > maxprofix:
                    maxprofix = temp
    return maxprofix
