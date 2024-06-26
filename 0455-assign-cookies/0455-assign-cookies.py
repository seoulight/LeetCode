class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookiesNums = len(s)
        if not cookiesNums:
            return 0
        g.sort()
        s.sort()
        
        maxNum = 0
        cookieIndex = cookiesNums - 1
        childIndex = len(g) - 1
        while cookieIndex >= 0 and childIndex >= 0:
            if s[cookieIndex] >= g[childIndex]:
                maxNum += 1
                cookieIndex -= 1
            childIndex -= 1
        return maxNum