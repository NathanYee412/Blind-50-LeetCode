class Solution:
    def merge(self, intervals):
        
        start = 0
        end = 1
        
        for i, x in enumerate(intervals):
            if(i < len(intervals) - 1):
                y = intervals[i+1]
                if(x[end] >= y[start] and x[end] <= y[end]):
                    
                    mStart = min(x[start], y[start])
                    mEnd = max(x[end], y[end])
                    intervals[i] = [mStart, mEnd]
                    del intervals[i+1]
                    
        return intervals

def main():

    test = Solution()

    # Test Cases
    t1 = [[1,4],[0,1]]
    t1Expected = [[0,4]]

    print("Test #1: [[1,4],[0,1]]")
    if test.merge(t1) == t1Expected:
        print("Pass")
    else:
        print("Fail")


    print("Test #1: [[1,3],[2,6],[8,10],[15,18]]")
    t2 = [[1,3],[2,6],[8,10],[15,18]]
    t2Expected = [[1,6],[8,10],[15,18]]
    if test.merge(t2) == t2Expected:
        print("Pass")
    else:
        print("Fail")


    


    return 0


if __name__ == "__main__":
    main()