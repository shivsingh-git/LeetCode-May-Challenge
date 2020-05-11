class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        count=0
        if((c[1][0]-c[0][0])==0):
            for i in range (0,len(c)):
                if(c[i][0]==c[0][0]):
                    count+=1

        elif((c[1][1]--c[0][1])==0):
            for i in range(0,len(c)):
                if(c[i][1]==c[0][1]):
                    count+=1

        else:            
            m=(c[1][1]-c[0][1])/(c[1][0]-c[0][0])
            for i in range (0,len(c)):
                if((c[i][1]-c[0][1])==m*(c[i][0]-c[0][0])):
                    count+=1
                
        if (count==len(c)):
            return True
        else:
            return False
