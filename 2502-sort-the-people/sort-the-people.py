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
        l=len(names)
        for i in range(1,l):
            keyh=heights[i]
            keyn=names[i]
            j=i-1
            while j>=0 and keyh>heights[j]:
                heights[j+1]=heights[j]
                names[j+1]=names[j]
                j-=1
            heights[j+1]=keyh
            names[j+1]=keyn
        return names    
