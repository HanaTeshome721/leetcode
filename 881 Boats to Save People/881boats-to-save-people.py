class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people.sort()
        # r=len(people)-1
        # l=0
        # cnt=0
        # while l<=r:
        #     s= people[r]+people[l]
        #     if s<=limit:
        #         cnt+=1
        #         l+=1
        #         r-=1
        #     elif s>limit:
        #         cnt+=1
        #         r-=1
        # return cnt       

    #    people.sort()
    #    l=0
    #    r=len(people)-1
    #    cnt=0 
    #    while l<=r:
    #       remain=limit-people[r]
    #       cnt+=1
    #       r-=1
    #       if l<=r and remain>=people[l]:
    #         l+=1
    #    return cnt 
        # people.sort()
        # l=0
        # r=len(people)-1
        # cnt=0
        # while l<=r:
        #     w=people[l]+people[r]
        #     if w<=limit:
        #         l+=1
        #     r-=1
        #     cnt+=1
        # return cnt        
        
        people.sort()
        count=0
        l=0
        r=len(people)-1
        while l<=r:
            if l==r:
                return count+1
            if people[l]+people[r]>limit:
                r-=1
            else:
                r-=1
                l+=1
            count+=1  

        return count          











    #  count=0
    #  l=0
    #  r=len(people)-1
    #  people.sort()
    #  while l<=r:
    #     if l==r:
    #       return count+1
    #     elif people[r]+people[l]>limit:
    #         count+=1
    #         r-=1
    #     elif people[r]+people[l]<=limit:
    #         count+=1
    #         l+=1
    #         r-=1
    #  return count

            
        
       
             
