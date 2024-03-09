class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        
        idx1 = 0
        idx2 = 0
        while idx1 < len1 and idx2 < len2:
            if nums1[idx1] == nums2[idx2]:
                return nums1[idx1]
            while idx1 < len1 and nums1[idx1] < nums2[idx2]:
                idx1 += 1
            while idx1 < len1 and idx2 < len2 and nums2[idx2] < nums1[idx1]:
                idx2 += 1
        return -1
                
                