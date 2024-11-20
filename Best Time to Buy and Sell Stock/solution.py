def buySellStock(prices):

    maxProfit = 0
    i = 0
    j = 1

    while j < len(prices):

        if prices[i] < prices[j]:
            profit = prices[j] - prices[i]
            maxProfit = max(profit, maxProfit)
        else:
            i = j
        j += 1
    
    return maxProfit
print(buySellStock([7,1,5,3,6,4]))