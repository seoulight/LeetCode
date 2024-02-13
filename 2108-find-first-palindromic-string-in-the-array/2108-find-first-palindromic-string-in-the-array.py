class Solution:
    def is_palindrome(self, word: str) -> bool:
        n = len(word)
        for i in range(n // 2):
            if word[i] != word[n - i - 1]:
                return False
        return True
    
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""
        