class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    #   return  len(set(s))==len(set(t))==len(set(zip(s,t)))
    #   if len(set(t))!=len(set(s)):
    #     return False
    #   return [s.index(i) for i in s ]== [t.index(i) for i in t  ]

    #   mapts,mapst={},{}
    #   for i in range(len(s)):
    #     ct=t[i]
    #     cs=s[i]

    #     if (ct in mapts and mapts[ct]!=cs) or (cs in mapst and mapst[cs]!=ct):
    #         return False
    #     mapts[ct]=cs
    #     mapst[cs]=ct
    #   return True  

      smap={}
      taken=set()

      for i in range(len(s)):
        if s[i] in smap:
            if smap[s[i]]!=t[i]:
                return False
        else:
            if t[i] in taken:
                return False
            smap[s[i]]=t[i]
            taken.add(t[i])
      return True                  