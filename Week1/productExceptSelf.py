class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        sol = []
        l = 0
        r = len(nums) - 1
        lvalue = 1
        rvalue = 1
        
        while l < len(nums) and r >= 0:
            prefix.append(lvalue)
            lvalue = lvalue * nums[l]      
            l += 1
            
            postfix.insert(0, rvalue)
            rvalue = rvalue * nums[r]
            r -= 1
            
        
        for i in range(0, len(prefix)):
            val = prefix[i] * postfix[i]
            sol.append(val)
            
        return sol 