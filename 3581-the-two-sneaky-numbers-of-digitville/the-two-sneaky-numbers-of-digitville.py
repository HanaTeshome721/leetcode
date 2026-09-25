class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        m=[]
        cnt=Counter(nums)
        for v,c in cnt.items():
            if c==2:
                m.append(v)
        return m        