class Solution:
    def minimumLength(self, s: str) -> int:
        s_temp = s
        while len(s_temp) > 1:
            prefix = s_temp[0]
            l, r = 0, len(s_temp) - 1
            if l >= len(s_temp) or r < 0 or s_temp[l] != s_temp[r]:
                break
            while l < len(s_temp) and s_temp[l] == prefix:
                l += 1
            while 0 <= r and s_temp[r] == prefix:
                r -= 1
            s_temp = s_temp[l:r+1]
        return len(s_temp)
            
                
            