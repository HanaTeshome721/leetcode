class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sd=defaultdict(list)
        for  i,s in enumerate(strs):
           st="".join(sorted(s))
           if st in sd:
              sd[st].append(i)
           else:
            sd[st]=[i]
        ans=[]
        for v,idx in sd.items():
            ag=[]
            for i in idx:
                ag.append(strs[i])
            ans.append(ag)
        return ans             