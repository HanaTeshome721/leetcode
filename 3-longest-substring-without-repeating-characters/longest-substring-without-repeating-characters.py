class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       w=[]
       mx=0
       for hc in s:
            while hc in w:
                w.pop(0)
            w.append(hc)
            mx=max(mx,len(w))    
       return mx     