class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        lg=len(skill)
        sm=sum(skill)

        if sm%(lg//2):
          return -1

        res=0
        skill.sort()
        l=0
        r=lg-1
        t=sm//(lg//2)
        while l<=r:
            if skill[l]+skill[r]==t:
                res+=skill[l]*skill[r]
            else:
                return -1
            r-=1
            l+=1
        return res    

