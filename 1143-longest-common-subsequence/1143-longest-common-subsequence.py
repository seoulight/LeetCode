class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        lcs = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    lcs[i + 1][j + 1] = lcs[i][j] + 1
                else:
                    lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i + 1][j])
        return lcs[n1][n2]
                