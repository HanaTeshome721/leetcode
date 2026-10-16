class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        # buble
        # l=len(names)
        # for i in range(l):
        #     for j in range(l-i-1):
        #         if heights[j]<heights[j+1]:
        #             heights[j], heights[j+1]=heights[j+1],heights[j]
        #             names[j],names[j+1]=names[j+1],names[j]
        # return names

        # select
        # l=len(names)
        # for i in range(l):
        #     mx=i
        #     for j in range(i+1,l):
        #         if heights[j]>heights[mx]:
        #             mx=j
        #     heights[i],heights[mx]=heights[mx],heights[i]    
        #     names[i],names[mx]=names[mx],names[i]   
        # return names     
        
        # inseret
        # l=len(names)
        # for i in range(1,l):
        #     keyh=heights[i]
        #     keyn=names[i]
        #     j=i-1
        #     while j>=0 and keyh>heights[j]:
        #         heights[j+1]=heights[j]
        #         names[j+1]=names[j]
        #         j-=1
        #     heights[j+1]=keyh
        #     names[j+1]=keyn
        # return names    

         maxi=max(heights)
         count=[0]*(maxi+1)
         n=len(heights)

         sorted_name=[None]*n
        

         for h in heights:
            count[h]+=1

         indx=n-1

         for h in range(maxi+1):
            for _ in range(count[h]):
                orgindx=heights.index(h)
                sorted_name[indx]=names[orgindx]
                heights[orgindx]=-1
                indx-=1
         return sorted_name      