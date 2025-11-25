class Solution:
    def firstUniqChar(self, s: str) -> int:
        see=set()
        for i in range(len(s)):
            if (s[i]  not in s[i+1:] ) and ( s[i] not in see):
                return i
            see.add(s[i])
        return -1        