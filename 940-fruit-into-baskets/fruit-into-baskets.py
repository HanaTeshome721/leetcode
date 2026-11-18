class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count=defaultdict(int)
        l,res,total=0,0,0
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            total+=1

            if len(count)>2:
                f=fruits[l]
                count[f]-=1
                total-=1
                l+=1

                if  not count[f]:
                    count.pop(f)
            res=max(res,total)
        return res

        # m=0
        # my={}
        # l=0
        # r=0
        # while r<len(fruits):
        #     my[fruits[r]]=1+my.get(fruits[r],0)
        #     if len(my)>2:
        #         my[fruits[l]]-=1
        #         if my[fruits[l]]==0:
        #             del my[fruits[l]]
        #         l+=1    
        #     if len(my)<=2:
        #         m=max(m,r-l+1)
        #     r+=1    
        # return  m              



   

        # # f1, f2, ans, c1, c2, prev = -1, -1, 0, 0, 0, 0
        # # for f in fruits:
        # #     if f == f1:
        # #         c1 += 1
        # #         prev += 1
        # #     elif f == f2:
        # #         f1, f2 = f2, f1
        # #         c1, c2 = c2+1, c1
        # #         prev = 1
        # #     else:
        # #         if c1+c2 > ans: ans = c1+c2
        # #         f1, f2 = f, f1
        # #         c1, c2 = 1, prev
        # #         prev = 1
        # # return max(ans, c1+c2)