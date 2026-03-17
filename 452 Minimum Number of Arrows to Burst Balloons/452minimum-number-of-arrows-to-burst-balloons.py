class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
       arr=len(points)
       points.sort()
       prev=points[0]
       for cur in points[1:]:
           if cur[0]<=prev[1]:
            arr-=1
            prev=[cur[0],min(cur[1],prev[1])]
           else:
            prev=cur
       return arr     

