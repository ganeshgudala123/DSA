class Solution(object):  
    def romanToInt(self, s):  
        val = 0   
        prev_value=0
        for i in s:  
            if i == "I":  
                count = 1  
            elif i == "V":  
                count = 5  
            elif i == "X":  
                count = 10  
            elif i == "L":  
                count = 50  
            elif i == "C":  
                count = 100  
            elif i == "D":  
                count = 500  
            elif i == "M":  
                count = 1000  
            else:  
                continue 
            if count > prev_value:  
                val += count - 2 * prev_value 
            else:  
                val += count  
            prev_value = count  

        return val  