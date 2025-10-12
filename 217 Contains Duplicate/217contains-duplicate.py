class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    #    return len(nums)!=len(set(nums))
        # hash=defaultdict(int)
        # for i in nums:
        #     if i in hash:
        #         return True
        #     hash[i]+=1  
        # return False  

        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False          