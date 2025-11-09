class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # nums=[i for i in range(int(sqrt(c))+1)]
        # l=0
        # r=len(nums)-1
        # while l<=r:
        #     a= nums[l]**2 + nums[r]**2
        #     if a==c:
        #         return True
        #     elif a>c:
        #         r-=1
        #     else:
        #         l+=1        
            
        # return False   



    #    num=int(c**0.5)
    #    while num*num >c//2:
    #      target=(c-num*num)**0.5
    #      if target==int(target):
    #         return True
    #      num-=1
    #    return False 


    #    s=set()
    #    for i in range(int(sqrt(c))+1):
    #      s.add(i)
    #    for i in s:
    #      a=i*i
    #      b=(c-a)**0.5
    #      if b in s:
    #         return True 
    #    return False      

        l=0
        r=int(sqrt(c))
        while l<=r:
            a= l*l+r*r
            print(a,c)
            if a==c:
                return True
            if a>c:
                r-=1
            else:
                l+=1
        return False                


        


     
    
