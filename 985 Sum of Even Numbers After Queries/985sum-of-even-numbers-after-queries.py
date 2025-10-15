class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    #  s=sum([x for x in nums if x%2==0])
    #  ans=[]
    #  for v,i in queries:
    #     if nums[i]%2==0:
    #         s-=nums[i]
    #     nums[i]+=v
    #     if nums[i]%2==0:
    #         s+=nums[i]
    #     ans.append(s)
    #  return ans           

        answer = []
        ansnum = 0
        for x in nums:
            if x % 2 == 0:
                ansnum += x
        for v,i in queries:
            if nums[i] % 2 == 0:
                if v % 2 == 0:
                    ansnum += v
                else:
                    ansnum -= nums[i]
            else:
                if v % 2 == 1:
                    ansnum += v + nums[i]
            nums[i] += v
            answer.append(ansnum)
        return answer