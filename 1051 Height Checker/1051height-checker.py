class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        an=sorted(heights)
        cnt=0
        for i in range(len(an)):
            if heights[i]!=an[i]:
                cnt+=1
        return cnt        
