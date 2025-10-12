class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
       res={}
       for s in strs:
          key=''.join(sorted(s))
          res[key]=res.get(key,[])+[s]
        #   if key in res:
        #     res[key].append(s)
        #   else:
        #     res[key]=[s]
       return list(res.values())   
       res=defaultdict(list)
       for i in strs:
         cu=[0]*26
         for c in i:
            cu[ord(c)-ord('a')]+=1
         res[tuple(cu)].append(i)
         
       return list(res.values())           