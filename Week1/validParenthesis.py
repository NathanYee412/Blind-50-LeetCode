# using stack data structure
# create hash map to see if closing bracket matches the opening bracket

# neetcode solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        for c in s:
            print(stack)
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
    
    
    
def main():
    obj = Solution()

    obj.isValid('([{}])')

    temp = ['a', 'b', 'c']
    print(temp[-1])
    temp.append('d')
    print(temp[-1])

if __name__ == "__main__":
    main()