class Solution:
    def containsDuplicate(self, nums):
        numDict = {}
        
        for i, x in enumerate(nums):
            if x in numDict:
                return True
            else:
                numDict[x] = i
                
                
        return False