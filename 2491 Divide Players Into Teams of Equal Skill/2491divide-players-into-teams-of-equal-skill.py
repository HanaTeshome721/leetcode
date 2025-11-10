class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total=sum(skill)
        target=(total*2)//len(skill)

        if (total*2) % len(skill):
            return -1
        count=Counter(skill)           
        chm=0
        for r in range(len(skill)):
               s=skill[r]
               if not count[s]:
                  continue
               diff= target-s
               if not count[diff]:
                  return -1
               chm+=s*diff
               count[s]-=1
               count[diff]-=1
        return chm           
            
      
