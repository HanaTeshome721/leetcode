class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # piles.sort()
        # q=deque(piles)
        # cn=0
        # while len(q)>0:
        #     q.popleft()
        #     q.pop()
        #     cn+=q.pop()
        # return cn 



        # return sum(sorted(piles)[len(piles)//3::2])

        # piles.sort(reverse=True)
        # n=len(piles)
        # k=n//3
        # cn=0
        # for i in range(1,n-k,2):
        #     cn+=piles[i]
        # return cn    
        

        piles.sort()
        r=len(piles)-1
        l=0
        md=0
        an=0
        while l<r:
            md=r-1
            an+=piles[md]
            l+=1
            r-=2
        return an   




          
        









    
