import math

class Solution:
    def reverse(self, x: int) -> int:
        #computational complexity: O(N), we only need to iterate though the number of digits
        #space complexity: O(1) -- only requires storage to store one int
        ret = 0
        max_int = 2**31 -1
        min_int = - 2**31
        max_intDiv10 = int(max_int / 10)
        min_intDiv10 = int(min_int / 10)
        max_lastDigit = max_int%10
        min_lastDigit = min_int%10
    
            
        while x!=0:
            #(1) pop out an integer using %
            pop = int(math.fmod(x,10)) #using math.fmod in favor of % 
            x = int(x/10)
            
            #(2) check out of boundary case
            if max_intDiv10 < ret or (max_intDiv10 == ret and pop > 7):
                return 0
            elif min_intDiv10 > ret or (min_intDiv10 == ret and pop <-8):
                return 0
            #(3) push into new ret
            ret = ret * 10 + pop
            
        return ret