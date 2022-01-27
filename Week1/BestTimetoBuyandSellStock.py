# My solution using two while loops

class Solution:
    def maxProfit(self, prices) -> int:
        # left and right pointer
        l, r = 0, 1
        
        maxDayIndex = 0
        maxDayPrice = 0
        minDayIndex = 0
        minDayPrice = 10000
        
        while r != (len(prices) - 1):
            #find max profit past l
            if prices[r] > maxDayPrice:
                maxDayPrice = prices[r]
                maxDayIndex = r
            
            r += 1
        
        while l < maxDayIndex:
            #find min day before max day
            if prices[l] < minDayPrice:
                minDayPrice = prices[l]
                minDayIndex = l
            
            l += 1
        
        if prices[maxDayIndex] - prices[minDayIndex] <= 0:
            return 0
        else:
            return prices[maxDayIndex] - prices[minDayIndex]
        

# Correct solution
# Moving window using two pointers

class Solution:
    def maxProfit(self, prices) -> int:
        # left and right pointer
        l, r = 0, 1
        
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > maxP:
                    maxP = profit
            else:
                l = r
            
            r += 1
            
        return maxP
            