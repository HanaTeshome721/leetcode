class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # lock=defaultdict(list)
        # cnt=0
        # for i,v in enumerate(nums):
        #     for per in lock[v]:
        #         if per*i%k==0:
        #             cnt+=1
        #     lock[v].append(i)
        # return cnt   

        seen={}
        cnt=0
        for i,v in enumerate(nums):
            if seen.get(v,0):
                for j in seen[v]:
                    if j*i%k==0:
                     cnt+=1
                seen[v].append(i)
                
            else:
                seen[v]=[i]
        return cnt             