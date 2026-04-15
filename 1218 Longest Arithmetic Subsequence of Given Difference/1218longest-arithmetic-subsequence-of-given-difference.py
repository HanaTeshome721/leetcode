class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
      n=len(arr)
      dp={}
      ans=0
      for a in arr:
          target=a-difference
          if not target in dp:
            dp[a]=1
          else:
             dp[a]=1+dp[target]
          ans=max(ans,dp[a])
      return ans        