class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        n = len(intervals)
        answer = []
        i = 0
        while i < n:
            start, end = intervals[i][0], intervals[i][1]
            if new_end < start:
                break
            if end < new_start:
                answer.append([start, end])
            else:
                if start <= new_start <= end:
                    new_start = min(start, new_start)
                if start <= new_end <= end:
                    new_end = max(end, new_end) 
            i += 1
        answer.append([new_start, new_end])
        answer += intervals[i:]
        return answer
            