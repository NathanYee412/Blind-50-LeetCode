class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s)
        s = s.lower()
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            print(s[l], s[r])            
            if s[l] == s[r]:
                l += 1
                r -= 1
                
            else:
                return False

        return True