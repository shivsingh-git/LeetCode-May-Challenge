class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num).replace("0b","")
        c=''
        for i in range(len(b)):
            if(b[i]=="1"):
                c += "0"
            else:
                c += "1"
                
        return(int(c,2))      
