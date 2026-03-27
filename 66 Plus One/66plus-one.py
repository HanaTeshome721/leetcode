class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=''.join(map(str,digits))
        num=int(num)+1
        ans=[]
        for a in str(num):
            ans.append(int(a))
        return ans    