class Solution:
    def lengthOfLastWord(self, s: str) -> int:   
        r = len(s) - 1
        count = 0
        start = False
        
        while r >= 0:
            
            if s[r].isalpha() and s[r] != ' ' and start == False:
                count += 1
                start = True
                
            elif s[r].isalpha() and s[r] != ' ' and start == True:
                count += 1
                
            if s[r] == ' ' and start == True:
                break
            
            r -= 1
                
            
                
        return count
            
            
            
            
            
            
        
            
            