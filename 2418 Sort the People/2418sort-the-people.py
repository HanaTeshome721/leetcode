class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # bubble
        n=len(heights)
        for i in range(n):
            for j in range(n-1-i):
                if heights[j+1]>heights[j]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
                    names[j],names[j+1]=names[j+1],names[j]
        return names            

        # selecton
        # for i in range(n):
        #     mindx=i
        #     for j in range(i+1,n):
        #         if heights[j]>heights[mindx]:
        #             mindx=j  
        #     heights[i],heights[mindx]=heights[mindx],heights[i]
        #     names[i],names[mindx]=names[mindx],names[i]
        # return names      

        # insertion
        # for i in range(1,n):
        #     key=heights[i]
        #     keyn=names[i]
        #     j=i-1

        #     while j>-1 and heights[j]<key:
        #         heights[j+1]=heights[j]
        #         names[j+1]=names[j]
        #         j-=1
        #     heights[j+1]=key
        #     names[j+1]=keyn  
        # return names       

        # counting
        #  maxi=max(heights)
        #  count=[0]*(maxi+1)
        #  n=len(heights)

        #  sorted_name=[None]*n
        #  sorted_heights=[0]*n

        #  for h in heights:
        #     count[h]+=1

        #  indx=n-1

        #  for h in range(maxi+1):
        #     for _ in range(count[h]):
        #         orgindx=heights.index(h)
        #         sorted_heights[indx]=h
        #         sorted_name[indx]=names[orgindx]
        #         heights[orgindx]=-1
        #         indx-=1
        #  return sorted_name          