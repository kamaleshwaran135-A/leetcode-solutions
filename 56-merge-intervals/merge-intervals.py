class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = result[-1][1]
            
            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])
        
        return result