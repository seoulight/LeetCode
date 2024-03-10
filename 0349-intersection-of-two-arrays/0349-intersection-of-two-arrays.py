class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        for num in nums1:
            if num in nums2:
                answer.add(num)
        return answer