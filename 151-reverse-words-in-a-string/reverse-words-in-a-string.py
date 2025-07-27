class Solution:
    def reverseWords(self, s: str) -> str:
        gane=s.split()[::-1]
        result=""
        for i in gane:
            result+=str(i)
        result=" ".join(gane)
        return result