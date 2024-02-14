class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_idx = 0
        neg_idx = 0
        answer = []
        n = len(nums)
        while (pos_idx < n and neg_idx < n):
            while (pos_idx < n and nums[pos_idx] < 0):
                pos_idx += 1
            answer.append(nums[pos_idx])
            pos_idx += 1
            while (neg_idx < n and nums[neg_idx] > 0):
                neg_idx += 1
            answer.append(nums[neg_idx])
            neg_idx +=1 
            
        return answer