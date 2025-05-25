class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[0])

        merged = [intervals[0]]

        count = 0
        for i in range(1, len(intervals)):
            prev_start, prev_end = merged[-1]
            curr_start, curr_end = intervals[i]

            if prev_end > curr_start:
                merged[-1][1] = min(prev_end, curr_end)
                count += 1
            else:
                merged.append([curr_start, curr_end])
        
        return count
            


            