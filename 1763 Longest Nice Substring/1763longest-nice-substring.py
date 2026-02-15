class Solution:
    def longestNiceSubstring(self, s: str) -> str:
       if len(s)<2:
         return ""

       s_set=set(s)
       for i,c in enumerate(s):
            if c.swapcase() not in s_set:
                left=self.longestNiceSubstring(s[i+1:])  
                right=self.longestNiceSubstring(s[:i]) 
                return left if len(left)>len(right) else right
       return s 
        # s_set = set(s)
        # for i in range(len(s)):
        #     if s[i].lower() not in s_set or s[i].upper() not in s_set:
        #         left_lns = self.longestNiceSubstring(s[:i])
        #         right_lns = self.longestNiceSubstring(s[i+1:])
        #         return max(left_lns, right_lns, key=len)
        # return s