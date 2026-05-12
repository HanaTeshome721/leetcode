class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    #    res=[]
    #    cur=[]
    #    def backtrack(i):
    #         if i >=len(nums):
    #             res.append(cur.copy())
    #             return 
    #         cur.append(nums[i])
    #         backtrack(i+1)
    #         cur.pop()
    #         backtrack(i+1)
    #    backtrack(0)
    #    return res  


    #    res=[]
    #    def btk(i,path):
    #         res.append(path[:])
    #         for i in range(i,len(nums)):
    #             path.append(nums[i])
    #             btk(i+1,path)
    #             path.pop()
    #    btk(0,[])         
    #    return res     


    #    def dfs(i,path,length):
    #     if length==len(path):
    #         ans.append(path[:])
    #         return 
    #     for j in range(i,len(nums)):
    #         path.append(nums[j])
    #         dfs(j+1,path,length)
    #         path.pop()

    #    ans=[]
    #    for l in range(len(nums)+1):
    #        dfs(0,[],l)
    #    return ans           

        n=len(nums)
        res=[]
        for mask in range(1<<n):
            subset=[]
            for i in range(n):
                if mask & (1<<i):
                    subset.append(nums[i])
            res.append(subset)
        return res            

