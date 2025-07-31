class Solution:
    def isPalindrome(self, s: str) -> bool:
        gane=s.split()
        result=""
        result1=[]
        for i in gane:
            result+=str(i)
        result="".join(gane)
        for i in result:
            if i.isalnum():
                result1.append(i)
        result2="".join(result1)
        result2=result2.lower()
        for i in range(len(result2)//2):
            if result2[i] != result2[len(result2) - 1 - i]:
                return False
        return True