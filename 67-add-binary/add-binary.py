class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=int(a,2)
        d=int(b,2)
        sum1=c+d
        result=bin(sum1)[2:]
        return result