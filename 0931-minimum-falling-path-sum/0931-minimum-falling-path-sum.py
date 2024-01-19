class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for r in range(n - 2, -1, -1):
            for c in range(n):
                best = matrix[r + 1][c]
                if c > 0:
                    best = min(best, matrix[r + 1][c - 1])
                if c + 1 < n:
                    best = min(best, matrix[r + 1][c + 1])
                matrix[r][c] += best
        answer = sys.maxsize
        
        for i in range(n):
            answer = min(answer, matrix[0][i])
        return answer
                
            