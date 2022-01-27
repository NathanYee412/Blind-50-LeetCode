class Solution:
    def maxProfit(self, prices) -> int:
        # left and right pointer
        l, r = 0, len(prices) - 1
        
        lowDay = 10000
        highDay = 0
        
        while l < r:
            if prices[l] < lowDay:
                lowDay = prices[l]
                
            if prices[r] > highDay:
                highDay = prices[r]
                
            l += 1
            r -= 1
            
        if highDay - lowDay < 0:
            return 0
        else:
            return highDay - lowDay