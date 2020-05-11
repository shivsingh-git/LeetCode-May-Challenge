import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<0:
            return false
        else:
            sqr=math.sqrt(num)                                      #square root of that
            return((sqr - math.floor(sqr)) == 0)                    #if it eqaul to zero subtracted from the floor of the number then true
