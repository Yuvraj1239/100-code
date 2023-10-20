class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def sol(a,b):
    
            
            count = 0
            if(b[0]==a[0]):
                count = count+1
            else:
                for i in range(len(points)):

                    if(points[i][1]==((b[1]-a[1])/(b[0]-a[0]))*points[i][0]):
                        print(points[i])
                        count = count+1
            return count
        max  = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if(max<sol(points[i],points[j])):
                    max = sol(points[i],points[j])
        return max
