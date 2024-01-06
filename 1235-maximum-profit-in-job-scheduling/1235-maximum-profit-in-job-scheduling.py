class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        number_of_jobs = len(profit)
        dp = [0] * (number_of_jobs + 1)
        for i, (curr_end_time, curr_start_time, curr_profit) in enumerate(jobs):
            index = bisect_right(jobs, curr_start_time, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[index] + curr_profit)
        return dp[number_of_jobs]