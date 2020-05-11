class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        count=0
        if((c[1][0]-c[0][0])==0):                              #if the slope is infinity means the line parallel to the y axis.
            for i in range (0,len(c)):
                if(c[i][0]==c[0][0]):
                    count+=1

        elif((c[1][1]--c[0][1])==0):                           #if the sloop is zero anyline parellel to x axis.
            for i in range(0,len(c)):
                if(c[i][1]==c[0][1]):
                    count+=1

        else:            
            m=(c[1][1]-c[0][1])/(c[1][0]-c[0][0])             #in all the other cases calculating the slope of the line by frst two points.
            for i in range (0,len(c)):
                if((c[i][1]-c[0][1])==m*(c[i][0]-c[0][0])):   #satisfying the equatin,(y-y1)=m(x-x1)
                    count+=1                                  #counting the value if all the value satisfies
                
        if (count==len(c)):                                   #if all the values satisfies the given eqaution then return true
            return True
        else:
            return False
