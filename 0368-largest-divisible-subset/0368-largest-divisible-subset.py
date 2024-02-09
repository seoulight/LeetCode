class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_index = 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if (dp[max_index] < dp[i]):
                        max_index = i
        answer = []
        num = nums[max_index]
        max_size = dp[max_index]
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                answer.append(nums[i])
                num = nums[i]
                max_size -= 1
        return answer
                
            