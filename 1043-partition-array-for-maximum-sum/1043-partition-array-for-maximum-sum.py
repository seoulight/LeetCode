class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        dp = [0] * (k + 1)
        for start in range(n - 1, -1, -1):
            curr_max = 0
            end = min(n, start + k)
            
            for i in range(start, end):
                curr_max = max(arr[i], curr_max)
                dp[start % (k + 1)] = max(dp[start % (k + 1)], dp[(i + 1) % (k + 1)] + curr_max * (i - start + 1))
            print(dp)
        return dp[0]