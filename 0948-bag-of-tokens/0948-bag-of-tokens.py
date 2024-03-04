class Solution:        
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l_ptr = 0
        r_ptr = len(tokens) - 1
        score = 0
        max_score = 0
        while l_ptr <= r_ptr:
            if power >= tokens[l_ptr]:
                power -= tokens[l_ptr]
                score += 1
                l_ptr += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[r_ptr]
                score -= 1
                r_ptr -= 1
            else:
                break
            
        return max_score
        