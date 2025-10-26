class Solution:
    def maxArea(self, height: List[int]) -> int:
    #    res=0
    #    l=0
    #    r=len(height)-1
    #    while l<r:
    #     area=(r-l)* min(height[r],height[l])
    #     res=max(res,area)

    #     if height[l]<height[r]:
    #         l+=1
    #     else:
    #         r-=1
    #    return res    


        l, r = 0, len(height) - 1
        max_area = (r - l) * min(height[l], height[r])
        while r > l:
            print(l, r)
            if (r - l) * min(height[l], height[r]) > max_area:
                max_area = (r - l) * min(height[l], height[r])
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area    

        # res = 0
        # l = 0
        # r = len(height)-1
        # maxh = max(height)

        # while l<r:
        #     area = min(height[l],height[r]) * (r-l)
        #     res = max(area,res)

        #     if height[l] <= height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        #     if maxh * (r-l) < res:
        #         break
        # return res 