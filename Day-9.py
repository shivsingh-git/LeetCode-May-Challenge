import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<0:
            return false
        else:
            sqr=math.sqrt(num)
            return((sqr - math.floor(sqr)) == 0)
            
        
