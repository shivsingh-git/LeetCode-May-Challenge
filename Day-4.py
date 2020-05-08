#Number Complement
#Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
#Example 1
#Input: 5
#Output: 2
#Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2
#Input: 1
#Output: 0
#Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
#Note:
#The given integer is guaranteed to fit within the range of a 32-bit signed integer.
#You could assume no leading zero bit in the integer’s binary representation.

class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num).replace("0b","")                                         #converting the number to binary and replacing frst two digits
        c=''
        for i in range(len(b)):
            if(b[i]=="1"):                                                  #changing 0 to 1 and 1 to 0
                c += "0"
            else:
                c += "1"
                
        return(int(c,2))                                                   #returning the value in the int format      
