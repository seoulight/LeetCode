class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1:
            prefix = s[0]
            l, r = 0, len(s) - 1
            if l >= len(s) or r < 0 or s[l] != s[r]:
                break
            while l < len(s) and s[l] == prefix:
                l += 1
            while 0 <= r and s[r] == prefix:
                r -= 1
            s = s[l:r+1]
        return len(s)
            
                
            