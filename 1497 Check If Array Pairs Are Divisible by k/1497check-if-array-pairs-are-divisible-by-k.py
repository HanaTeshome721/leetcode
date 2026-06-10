class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt=Counter([x%k for x in arr])
        for r in cnt:
            if r==0 or r*2==k:
                if cnt[r]%2!=0:
                    return False
            else:
                if cnt[r]!=cnt[k-r]:
                    return False
        return True                    
