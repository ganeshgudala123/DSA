class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=0
        for digit in digits:
            result=result*10+digit
        result+=1
        result_list=[int(char) for char in str(result)]
        return result_list