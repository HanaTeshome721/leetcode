class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f=defaultdict(int)
        l=0
        ma=total=0
        for r in range(len(fruits)):
            f[fruits[r]]+=1
            total+=1
            while len(f)>2:
                rf=fruits[l]
                f[rf]-=1
                total-=1
                if not  f[rf]:
                    del f[rf]
                l+=1
            ma=max(total,ma)    
        return ma           