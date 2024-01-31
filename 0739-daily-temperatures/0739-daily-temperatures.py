from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = deque()
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 1, -1, -1):
            if not q:
                q.appendleft(i)
                res[i] = 0
            else:
                while q and temperatures[i] >= temperatures[q[0]]:
                    q.popleft()
                if not q:
                    res[i] = 0
                else:
                    res[i] = q[0] - i
                q.appendleft(i)
        return res