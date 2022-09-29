class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        output.append(intervals[0])
        for i in range(1,len(intervals)):
            if output[-1][1] >= intervals[i][0]:
                output[-1][1] = max(output[-1][1] , intervals[i][1])
            else:
                output.append(intervals[i])
        return output
        
        
