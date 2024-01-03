class Solution:    
    def numberOfBeams(self, bank: List[str]) -> int:
        answer = 0
        bank = [[int(device) for device in col] for col in bank]
        prev = sum(bank[0])
        for i in range(1, len(bank)):
            curr = sum(bank[i])
            if curr > 0:
                answer += prev * curr
                prev = curr
        return answer