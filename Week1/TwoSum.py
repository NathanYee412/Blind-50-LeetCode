class Solution:
    def twoSum(self, nums, target):
        
        vals = {} # nums[i] : index
        
        for i, x in enumerate(nums):
            
            # find the difference every loop
            diff = target - x 
            
            # check if the difference exists in the vals dict
            if diff in vals:
                # return current index and vals dict value
                return [i, vals[diff]]
            else:

                # else, add current value to the dict
                vals[x] = i
                
                
        return 