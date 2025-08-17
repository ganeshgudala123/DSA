class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            s=str(x)
            hi = s[::-1]
            if int(hi) == x:
                return True
            else:
                return False