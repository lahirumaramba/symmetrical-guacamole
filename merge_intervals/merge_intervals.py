class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
                continue
                
            end = max(merged[-1][1], interval[1])
            merged[-1][1] = end
            
        return merged
        
 #input = [[1,3],[2,6],[8,10],[15,18]]
 #output = [[1,6],[8,10],[15,18]]
