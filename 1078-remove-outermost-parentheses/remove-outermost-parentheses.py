class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        count=0
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            else:
                count-=1
            if (count == 0 or count ==1 and s[i]=='('):
                continue
            else:
                ans=ans+s[i]
        return ans