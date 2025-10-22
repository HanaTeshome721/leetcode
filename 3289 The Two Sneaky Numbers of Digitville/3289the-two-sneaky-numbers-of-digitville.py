class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
       nums.sort()
       snk=[]
       for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
              snk.append(nums[i-1])
            if len(snk)==2:
                return snk  


        # see=set()
        # du=set()
        # for i in nums:
        #     if i in see:
        #         du.add(i)
        #     else:
        #         see.add(i)
        # return list(du)                    