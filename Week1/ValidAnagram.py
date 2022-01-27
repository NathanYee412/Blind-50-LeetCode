class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False
        
        for x in s:
            
            for i in range(0, len(t)):
                if(x == t[i]):
                    t = t[:i] + t[i + 1:]
                    break
                
        if t == "":
            return True
        else:
            return False