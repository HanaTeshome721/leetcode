class Solution:
    def numRabbits(self, answers: List[int]) -> int:
       count=Counter(answers)
       res=0
       for x,c in count.items():
         gsize=x+1
         groups=(c+gsize-1)//gsize
         res+=gsize*groups
       return res   
       