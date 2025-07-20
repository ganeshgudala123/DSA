class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        A=s.strip().split()[-1]
        return len(A)