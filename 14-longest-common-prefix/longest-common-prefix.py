class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        for i in range(len(strs[0])):
            if  i<len(strs[-1]) and strs[0][i]!=strs[-1][i]:
                return strs[0][:i]
        return strs[0]        